"""
Module to factorize matrices

Functions
---------
`nmf`: Non-negative matrix factorization

"""
import numpy
import pymf

def nmf(data, iterations=10, num_bases=2):
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
    nmf_mdl = pymf.NMF(data, num_bases=num_bases, niter=iterations)
    nmf_mdl.initialization()
    nmf_mdl.factorize()
    return nmf_mdl.W, nmf_mdl.H