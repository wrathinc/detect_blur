# Detect_Blur
  Sorts images into folders based on the Laplacian of the image and then return the focus.


# Laplacian Operator
  From the explanation above, we deduce that the second derivative can be used to detect edges. 
  Since images are "*2D*", we would need to take the derivative in both dimensions. Here,
  the Laplacian operator comes handy.
  The Laplacian operator is defined by:

                                Laplace(f)=∂2f∂x2+∂2f∂y2
                                
The Laplacian operator is implemented in OpenCV by the function *Laplacian()* . In fact, since the Laplacian uses the gradient of images, it calls internally the Sobel operator to perform its computation.
