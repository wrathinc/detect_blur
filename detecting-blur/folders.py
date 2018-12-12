import os
class __folder__():

    def create_folders(self):

        '''
        function to create dir

        Parameters
        ----------
        none    

        Attributes
        ----------
        arg : os.dir 
            This is where we store arg,
        '''

        blurry_pics = "blury_photo"
        not_blurry_photo = "not_blurry"
        image_folder = "images"

        if not os.path.exists(blurry_pics):
            os.mkdir(blurry_pics)

        if not os.path.exists(not_blurry_photo):
            os.mkdir(not_blurry_photo)

        if not os.path.exists(image_folder):
            os.mkdir(image_folder)


