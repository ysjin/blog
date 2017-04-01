Title: Transforms in Video Codecs
status: draft
Date: 2016-04-08
Modified: 2016-04-08 
Category: science
Tags: python, video

Discrete Fourier Transform (DFT) and Discrete Cosine Transform (DCT)

## DFT
$$ X_k = \sum_{n=0}^{N-1} x_n e^{{-2j\pi kn}{N}} $$
where $ k \in Z $ and $ e^{\frac{-2j\pi kn}{N}} $ is expressed by the Euler's formula in the following:
$$ e^{\frac{-2j\pi kn}{N}} = cos(\frac{2\pi kn}{N}) + jsin(\frac{2\pi kn}{N}) $$

## DCT
DCT uses only real parts
$$ X_k = \sum_{n=0}^{N-1} x_n cos[\frac{\pi}{N} (n + \frac{1}{2}) k] $$
where $ k = 0, \ldots, N-1 $

DCT is used for natural image compression.
*Scipy* provides dct functions.

```python3
import numpy as np
from scipy.fftpack import dct

x = np.array([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
y = dct(x)
z = dct(y.transpose())
```

## H264/AVC Integer Transform


## H265/HEVC DCT Transform


## VP9 DCT Transform



