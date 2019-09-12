import SimpleITK as sitk
import numpy as np

class Resample_Class(object):
    '''
    Feed in images in form of #images, rows, cols
    '''
    def __init__(self):
        self.Resample = sitk.ResampleImageFilter()
    def resample_image(self,input_image, input_spacing=(0.975,0.975,2.5),output_spacing=(0.975,0.975,2.5),
                       is_annotation=False):
        '''
        :param input_image: Image of the shape # images, rows, cols
        :param spacing: Goes in the form of row spacing, col spacing, and then z_images (I know it's confusing..)
        :param is_annotation: Whether to use Linear or NearestNeighbor, Nearest should be used for annotations
        :return:
        '''
        output_spacing = np.asarray(output_spacing)
        self.Resample.SetOutputSpacing(output_spacing)
        if is_annotation:
            self.Resample.SetInterpolator(sitk.sitkNearestNeighbor)
        else:
            self.Resample.SetInterpolator(sitk.sitkLinear)

        image = sitk.GetImageFromArray(input_image)
        image.SetSpacing(input_spacing)
        orig_size = np.array(image.GetSize(),dtype=np.int)
        orig_spacing = np.asarray(image.GetSpacing())
        new_size = orig_size * (orig_spacing / output_spacing)
        new_size = np.ceil(new_size).astype(np.int)  # Image dimensions are in integers
        new_size = [np.int(i) for i in new_size]
        self.Resample.SetSize(new_size)
        self.Resample.SetOutputDirection(image.GetDirection())
        self.Resample.SetOutputOrigin(image.GetOrigin())
        output = self.Resample.Execute(image)
        output = sitk.GetArrayFromImage(output)
        return output

if __name__ == '__main__':
    # xxx = 1
    # Resample = Resample_Class()
    # image = np.zeros([68, 512,512])
    # image[30:40,126:256,125:256] = 1
    # k = Resample.resample_image(image,input_spacing=(0.975/2,0.975/2,2.5),output_spacing=(0.975,0.975,5),is_annotation=True)
    # xxx = 1