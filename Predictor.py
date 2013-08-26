"""
Module to generate and run signal predictors

Functions
---------
`levinson`: Generate predictor coefficients using the Levinson algorithm

`burg`: Generate predictor coefficients using the Burg algorithm

`predict`: Run an autoregressive linear predictor

"""
import spectrum
import scipy, numpy

def levinson(correlation, order):
    """
    Calculate the predictor coefficients for an autoregressive linear prediction
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
    coeffs, energy, reflectioncoeffs = spectrum.LEVINSON(correlation, order)
    energy /= correlation[0];
    return (coeffs,energy)

def burg(correlation, order):
    """
    Calculate the predictor coefficients for an autoregressive linear prediction
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
    coeffs, energy, reflectioncoeffs = spectrum.arburg(correlation, order)

    # These values are pure speculation
    energy /= correlation[0];
    # After this step, the curve looked like the one from levinson BEFORE THIS STEP.
    # This means we need to divide energy by it again. Also, the values are much much lower
    # than from levinson, the proportions are almost exactly the same. Ergo: multiply by the
    # ratio between them.
    energy *= (18600 / 42)
    energy /= correlation[0];
    energy = min(energy, 1)

    return (coeffs,energy)


def rls(x, n, order=4, lamb=1.0):
    """
    Recursive Least Squares Filter

    Parameters
    ----------
    x : numpy array
        Input signal.
    n : numpy array
        Noise signal.
    order : int
        Filter order.
    lamb : float
        Forgetting factor.

    Returns
    -------
    e : numpy array
        Filtered signal.

    """
    assert 0 < lamb <= 1, "lambda must be between 0 and 1"
    assert 0 < order, "order must be greater than zero"

    w = numpy.zeros(order)
    e = numpy.zeros_like(x)
    P = numpy.eye(order)

    for m in range(order, len(x)):
        # Acquire chunk of data
        y = n[m:m-order:-1];

        # Error signal equation
        e[m] = x[m]-numpy.dot(w.T, y);

        # Parameters for efficiency
        Pi = numpy.dot(P, y);

        # Filter gain vector update
        k = (Pi)/(lamb+numpy.dot(y.T, Pi));

        # Inverse correlation matrix update
        P = (P - numpy.dot(numpy.dot(k,y.T),P))*(1/lamb);

        # Filter coefficients adaption
        w = w + k*e[m];

    return e


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

     1. Create empty pred vector, padded by the number of coefficients at the end
     2. Pad original values by number of coefficients at both ends
     3. Crop data in each step accordingly
     4. Crop prediction

    """
    coeffs *= -1;
    pred = scipy.zeros_like(data)
    tmp = numpy.hstack(( scipy.zeros_like(coeffs), data ))

    for j in range(0, coeffs.size):
        offset = coeffs.size - j - 1
        pred = pred + coeffs[j] * tmp[offset:offset + len(pred)];

    return pred[:len(data)]