__author__ = 'Brian M Anderson'
# Created on 11/2/2020
import SimpleITK as sitk
import numpy as np


class Resampler(object):
    def __init__(self):
        self.Resample = sitk.ResampleImageFilter()
    def resample_image(self, input_image, ref_handle=None, input_spacing=None,output_spacing=(0.975,0.975,2.5),
                       is_annotation=False):
        """
        :param input_image: Image of the shape # images, rows, cols, or sitk.Image
        :param spacing: Goes in the form of (row_dim, col_dim, z_dim) (I know it's confusing..)
        :param is_annotation: Whether to use Linear or NearestNeighbor, Nearest should be used for annotations
        :return:
        """
        if type(input_image) is np.ndarray:
            image = sitk.GetImageFromArray(input_image)
        else:
            image = input_image
        if input_spacing is not None:
            image.SetSpacing(input_spacing)
        if ref_handle is not None:
            output_spacing = ref_handle.GetSpacing()
            image.SetDirection(ref_handle.GetDirection())
            image.SetOrigin(ref_handle.GetOrigin())
        self.Resample.SetOutputSpacing(output_spacing)
        if is_annotation:
            if type(input_image) is np.ndarray:
                input_image = input_image.astype('int8')
            self.Resample.SetInterpolator(sitk.sitkNearestNeighbor)
        else:
            self.Resample.SetInterpolator(sitk.sitkLinear)
        if ref_handle is None:
            output_spacing = np.asarray(output_spacing)
            orig_size = np.array(image.GetSize(),dtype=np.int)
            orig_spacing = np.asarray(image.GetSpacing())
            new_size = orig_size * (orig_spacing / output_spacing)
            new_size = np.ceil(new_size).astype(np.int)  # Image dimensions are in integers
            new_size = [np.int(i) for i in new_size]
        else:
            new_size = ref_handle.GetSize()
        self.Resample.SetSize(new_size)
        self.Resample.SetOutputDirection(image.GetDirection())
        self.Resample.SetOutputOrigin(image.GetOrigin())
        output = self.Resample.Execute(image)
        if type(input_image) is np.ndarray:
            output = sitk.GetArrayFromImage(output)
        return output


class Resample_Class_Object(Resampler):
    def __init__(self):
        print('Please move from using Resample_Class_Object to Resampler, same arguments are passed')
        super().__init__()


if __name__ == '__main__':
    pass
