__all__ = ['ced', 'iee', 'colorRetriever']
from processors.filters.cannyEdgeDetection import cannyEdgeDetection as ced
from processors.filters.increasedEdgeEnhancement import increasedEdgeEnhancement as iee
from processors.filters.colorRetriever import toRGB