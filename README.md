# Data cube visualization

Multi-band gridded data such as hyperspectral remote sensing data, but also multi-temporal gridded data, stored in data cubes require effective visualization techniques, in a way that dominant patterns of the interior structure of the data cube can be explored visually, such as marginal histograms.

The python script combined_marginal_histograms.py reads an image file (.tif) holding an arbitrary number of bands, and generates the marginal histograms of each band, and plots them cumulatively, in a stacked manner.
The script also creates heatmaps of these marginal histograms, stacked together, and a greyscale plot of the input image.
In the current version, the user can then assemble the image and marginal histogram plots manually. The following examples use hyperspectral image data from the HyRANK hyperspectral benchmark dataset (https://www2.isprs.org/commissions/comm3/wg4/hyrank/) and from the Washington D.C. HYDICE hyperspectral dataset (http://cobweb.ecn.purdue.edu/~biehl/Hyperspectral_Project.zip):

<img width="1000" alt="Margial histograms for each band, stacked on top of each other." src="https://github.com/johannesuhl/datacube_visualization/blob/main/stacked_marginal_histograms.jpg">
