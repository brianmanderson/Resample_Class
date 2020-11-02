"# Resample_Class" 
For resampling nifti images (likely for medical purposes)
## Installation
    pip install NiftiResampler
### Usage
    from NiftiResampler.ResampleTools import ImageResampler, sitk
    Resampler = ImageResampler()
    base_image = sitk.ReadImage(image_path)
    desired_dimensions = (0.975, 0.975, 5.0)
    
    resampled = Resampler.resample_image(base_image,input_spacing=(0.975/2,0.975/2,2.5),output_spacing=(0.975,0.975,5),is_annotation=True)

