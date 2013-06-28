import spectrum
import scipy, numpy

def levinson(corr, order):
    coeffs, energy, reflectioncoeffs = spectrum.LEVINSON(corr, order)
    energy /= corr[0];
    return (coeffs,energy)

def burg(corr, order):
    coeffs, energy, reflectioncoeffs = spectrum.arburg(corr, order)

    # These values are pure speculation
    energy /= corr[0];
    # After this step, the curve looked like the one from levinson BEFORE THIS STEP.
    # This means we need to divide energy by it again. Also, the values are much much lower
    # than from levinson, the proportions are almost exactly the same. Ergo: multiply by the
    # ratio between them.
    energy *= (18600 / 42)
    energy /= corr[0];
    energy = min(energy, 1)

    return (coeffs,energy)

def predict(sig, coeffs):
    # Autoregressive linear prediction
    #
    # Prediction works as follows:
    #
    #       P = a1+ a2+ a3+ a4
    #
    #       #   _   _   _   _
    #       #   #   _   _   _
    #       #   #   #   _   _
    #       # = # + # + # + _
    #       _   #   #   #   #
    #       _   _   #   #   #
    #       _   _   _   #   #
    #       _   _   _   _   #
    #
    # Where # is a number and _ is a "dont care"
    #
    # This means
    #
    #  1. Create empty pred vector, padded by the number of coefficients at the end
    #  2. Pad original values by number of coefficients at both ends
    #  3. Crop data in each step accordingly
    #  4. Crop prediction

    coeffs *= -1;
    pred = scipy.zeros_like(sig)
    tmp = numpy.hstack(( scipy.zeros_like(coeffs), sig ))

    for j in range(0, coeffs.size):
        offset = coeffs.size - j - 1
        pred = pred + coeffs[j] * tmp[offset:offset + len(pred)];

    return pred[:len(sig)]