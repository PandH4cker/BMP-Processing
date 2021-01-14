__all__ = ['ced', 'iee', 'colorRetriever', 'blur', 'emboss']
from processors.filters.cannyEdgeDetection import cannyEdgeDetection as ced
from processors.filters.increasedEdgeEnhancement import increasedEdgeEnhancement as iee
from processors.filters.colorRetriever import retrieveColor
from processors.filters import blur
from processors.filters.emboss import emboss