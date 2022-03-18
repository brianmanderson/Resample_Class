# Resample_Class

For resampling nifti images (likely for medical purposes)

## Installation

```
    pip install NiftiResampler
```

### Usage

```python
from NiftiResampler.ResampleTools import ImageResampler, sitk

Resampler = ImageResampler()
base_image = sitk.ReadImage(image_path)
desired_dimensions = (0.975, 0.975, 5.0)
resampled = Resampler.resample_image(input_image_handle=base_image, ref_resampling_handle=None,
                                     output_spacing=(0.975, 0.975, 5), interpolator='Linear', empty_value=-1024)
```
