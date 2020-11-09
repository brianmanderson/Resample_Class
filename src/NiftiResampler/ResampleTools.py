__author__ = 'Brian M Anderson'
# Created on 11/2/2020
import SimpleITK as sitk
import numpy as np


class ImageResampler(object):
    def __init__(self):
        self.Resampler = sitk.ResampleImageFilter()
    def resample_image(self, input_image_handle, ref_resampling_handle=None, output_spacing=None,
                       interpolator='Linear'):
        """
        :param input_image_handle: SimpleITK image handle that will be resampled
        :param ref_resampling_handle: a reference SimpleITK image handle that has the desired dimensions
        :param output_spacing: a tuple of spacing that is desired for the input_image to be resampled to
        :param interpolator: 'Linear' or 'Nearest'
        :return:
        """
        assert type(input_image_handle) is sitk.Image, 'You need to pass a SimpleITK image handle!'
        assert ref_resampling_handle is not None or output_spacing is not None, 'You need to either provide a ' \
                                                                                'reference handle for resample, or ' \
                                                                                'output_spacing'
        if output_spacing is None:
            output_spacing = ref_resampling_handle.GetSpacing()
        self.Resampler.SetOutputSpacing(output_spacing)
        if interpolator == 'Linear':
            self.Resampler.SetInterpolator(sitk.sitkLinear)
        elif interpolator == 'Nearest':
            self.Resampler.SetInterpolator(sitk.sitkNearestNeighbor)
        if ref_resampling_handle is not None:
            self.Resampler.SetOutputDirection(ref_resampling_handle.GetDirection())
            self.Resampler.SetOutputOrigin(ref_resampling_handle.GetOrigin())
            self.Resampler.SetSize(ref_resampling_handle.GetSize())
        else:
            orig_size = np.array(input_image_handle.GetSize(),dtype=np.int)
            orig_spacing = np.asarray(input_image_handle.GetSpacing())
            new_size = orig_size * (orig_spacing / output_spacing)
            new_size = np.ceil(new_size).astype(np.int)  # Image dimensions are in integers
            new_size = [np.int(i) for i in new_size]
            self.Resampler.SetSize(new_size)
        output = self.Resampler.Execute(input_image_handle)
        return output


class Resample_Class_Object(ImageResampler):
    def __init__(self):
        print('Please move from using Resample_Class_Object to Resampler, same arguments are passed')
        super().__init__()


if __name__ == '__main__':
    pass
