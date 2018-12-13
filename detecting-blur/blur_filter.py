import cv2
class blur_laplacian():
    ''' class blur_laplacian returns a variance score of float vaule bulr = 24.5 '''

    def laplacian(self):
        ''' Parameters
            src:	Source image.
            dst:	Destination image of the same size and the same number 
                of channels as src.

            ddepth:	Desired depth of the destination image.
            ksize:	Aperture size used to compute the second-derivative filters.
                    See getDerivKernels for details. 
                    The size must be positive and odd.
            scale:	Optional scale factor for the computed 
                    Laplacian values. By default,
                no scaling is applied. See getDerivKernels for details.
            delta:	Optional delta value that is added to the results
                prior to storing them in dst .
            borderType:	Pixel extrapolation method, see BorderTypes
            Python:
            dst	=	cv.Laplacian(	src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]]	)
        '''

        #raise ValueError("needs to be an np.array")
        return cv2.Laplacian(self, cv2.CV_64F).var()
