"""
Module to factorize matrices

"""
import pymf


def nmf(data, iterations=None, num_bases=None):
    """
    Calculate Non-negative matrix factorization that fulfills

    WH = V

    Parameters
    ----------
    data : numpy array
        Matrix V
    num_bases : int
        Number of clusters
    iterations : int
        Number of iterations

    Returns
    -------
    w : numpy array
        Matrix W
    h : numpy array
        Matrix H

    """
    if num_bases is None:
        num_bases = data.shape[1] - 1

    if iterations is None:
        iterations = num_bases // 2

    nmf_mdl = pymf.NMF(data, num_bases=num_bases)
    nmf_mdl.factorize(niter=iterations)
    return nmf_mdl.W, nmf_mdl.H
