"# Resample_Class" 
For resampling images and annotations for deep learning

Below is an example of turning a cube on a high resolution image into a low resolution image

    pip install NiftiResampler
    
    from NiftiResampler.ResampleTools import ImageResampler
    Resampler = ImageResampler()
    image = np.zeros([68, 512,512])
    image[30:40,126:256,125:256] = 1
    resampled = Resampler.resample_image(image,input_spacing=(0.975/2,0.975/2,2.5),output_spacing=(0.975,0.975,5),is_annotation=True)
