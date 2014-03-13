"""
Module to generate and run signal predictors

Functions
---------
`levinson`: Generate predictor coefficients using the Levinson algorithm

`burg`: Generate predictor coefficients using the Burg algorithm

`rls`: Recursive Least Squares filter

`predict`: Run an autoregressive linear predictor

"""
import spectrum
import scipy
import numpy


def levinson(correlation, order):
    """
    Calculate the predictor coefficients for autoregressive linear prediction
    using the Levinson-Durbin algorithm

    Parameters
    ----------
    correlation : numpy array
        The autocorrelation function of a signal.
    order : int
        The order of the prediction.

    Returns
    -------
    coeffs : numpy array
        The calculated prediction coefficients
    energy : float
        The estimated residual error energy after
        prediction

    Notes
    -----

    * The first coefficient, 1, is left out.

    """
    assert 0 < order, "order must be greater than zero"

    coeffs, energy, reflectioncoeffs = spectrum.LEVINSON(correlation, order)
    energy /= correlation[0]
    return (coeffs, energy)


def burg(correlation, order):
    """
    Calculate the predictor coefficients for autoregressive linear prediction
    using the Burg algorithm

    Parameters
    ----------
    correlation : numpy array
        The autocorrelation function of a signal.
    order : int
        The order of the prediction.

    Returns
    -------
    coeffs : numpy array
        The calculated prediction coefficients
    energy : float
        The estimated residual error energy after
        prediction

    Notes
    -----

    * The first coefficient, 1, is left out.

    """
    assert 0 < order, "order must be greater than zero"

    coeffs, energy, reflectioncoeffs = spectrum.arburg(correlation, order)

    # These values are pure speculation
    energy /= correlation[0]
    # After this step, the curve looked like the one from levinson BEFORE
    # THIS STEP. This means we need to divide energy by it again. Also,
    # the values are much much lower than from levinson, the proportions
    # are almost exactly the same. Ergo: multiply by the ratio between them.
    energy *= (18600 / 42)
    energy /= correlation[0]
    energy = min(energy, 1)

    return (coeffs, energy)


def rls(x, d, order=4, lamb=1.0):
    """
    Recursive Least Squares Filter

    Parameters
    ----------
    x : numpy array
        Input signal.
    d : numpy array
        Desired signal.
    order : int
        Filter order.
    lamb : float
        Forgetting factor.

    Returns
    -------
    w : numpy array
        Filter coefficients.
    e : numpy array
        Error signal.
    y : numpy array
        Estimated signal.

    References
    ----------
    .. [1] : http://www.mathworks.com/matlabcentral/fileexchange/25769-adaptive-filter
    .. [2] : http://www.mathworks.de/de/help/dsp/ref/adaptfilt.rls.html

    """
    assert 0 < lamb <= 1, "lambda must be between 0 and 1"
    assert 0 < order, "order must be greater than zero"

    w = numpy.zeros(order)
    e = numpy.zeros_like(x)
    y = numpy.zeros_like(x)
    P = numpy.eye(order)

    for m in range(order, len(x)):
        c = x[m:m - order:-1]
        Pi = numpy.dot(P, c)
        k = Pi / (lamb + numpy.dot(c.T, Pi))
        y[m] = numpy.dot(w.T, c)
        e[m] = d[m] - y[m]
        P = (P - numpy.dot(numpy.dot(k, c.T), P)) * (1 / lamb)
        w = w + k * e[m]

    return (w, e, y)


def predict(data, coeffs):
    """
    Calculate the an autoregressive linear prediction given the signal
    and the prediction coefficients.

    Parameters
    ----------
    data : numpy array
        The signal.
    coeffs : numpy array
        The prediction coefficients.

    Returns
    -------
    data : numpy array
        The predicted signal

    Notes
    -----

    * The first coefficient, 1, is assumed to be left out.

    Prediction works as follows:

          P = a1+ a2+ a3+ a4

          #   _   _   _   _
          #   #   _   _   _
          #   #   #   _   _
          # = # + # + # + _
          _   #   #   #   #
          _   _   #   #   #
          _   _   _   #   #
          _   _   _   _   #

    Where # is a number and _ is a "dont care"

    This means

     1. Create empty pred vector, padded by the number of coefficients
        at the end
     2. Pad original values by number of coefficients at both ends
     3. Crop data in each step accordingly
     4. Crop prediction

    """
    coeffs *= -1
    pred = scipy.zeros_like(data)
    tmp = numpy.hstack((scipy.zeros_like(coeffs), data))

    for j in range(0, coeffs.size):
        offset = coeffs.size - j - 1
        pred = pred + coeffs[j] * tmp[offset:offset + len(pred)]

    return pred[:len(data)]
