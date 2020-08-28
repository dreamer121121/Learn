import numpy as np

def conv_forward_naive(x, w, b, conv_param):
    """
    A naive implementation of the forward pass for a convolutional layer.
    The input consists of N data points, each with C channels, height H and width
    W. We convolve each input with F different filters, where each filter spans
    all C channels and has height HH and width HH.
    Input:
    - x: Input data of shape (N, C, H, W)
    - w: Filter weights of shape (F, C, HH, WW)
    - b: Biases, of shape (F,)
    - conv_param: A dictionary with the following keys:
      - 'stride': The number of pixels between adjacent receptive fields in the
        horizontal and vertical directions.
      - 'pad': The number of pixels that will be used to zero-pad the input.
    Returns a tuple of:
    - out: Output data, of shape (N, F, H', W') where H' and W' are given by
      H' = 1 + (H + 2 * pad - HH) / stride
      W' = 1 + (W + 2 * pad - WW) / stride
    - cache: (x, w, b, conv_param)
    """

    N, C, H, W = x.shape
    F, _, HH, WW = w.shape
    S = conv_param['stride']
    P = conv_param['pad']
    # print("S",S)
    # print("P",P)
    Ho = 1 + (H - HH + 2 * P) // S
    Wo = 1 + (W - WW + 2 * P) // S
    x_pad = np.zeros((N, C, H + 2 * P, W + 2 * P)) #构建一张零矩阵图
    x_pad[:, :, P:P + H, P:P + W] = x
    print("x_pad",x_pad[0][0])
    # x_pad = np.pad(x, ((0,), (0,), (P,), (P,)), 'constant')
    out = np.zeros((N, F, Ho, Wo))
    for f in range(F):
        for i in range(Ho):
            for j in range(Wo):
                # N*C*HH*WW, C*HH*WW = N*C*HH*WW, sum -> N*1
                out[:, f, i, j] = np.sum(x_pad[:, :, i * S: i * S + HH, j * S: j * S + WW] * w[f, :, :, :],
                                         axis=(1, 2, 3))
        out[:, f, :, :] += b[f]
    cache = (x, w, b, conv_param)
    return out, cache

x = np.random.randn()
print(x[0][0])
w = np.random.randn(6,3,3,3)
params = {'stride':1,'pad':1}
bias = [0,0,0,0,0,0]
out = conv_forward_naive(x,w,bias,params)
print(out[0].shape)

