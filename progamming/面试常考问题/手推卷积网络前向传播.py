import numpy as np

def forward(w,x,b,params):
    P = params['padding']
    S = params['stride']
    (N,C,W,H) = x.shape
    x_pad = np.zeros((N,C,W+2*P,H+2*P))
    x_pad[:,:,P:W+P,P:H+P]=x #进行padding后的输入特征图
    (C_out,C_in,kw,kh) = w.shape
    W_out = (W-kw+2*P)//S+1
    H_out = (H-kh+2*P)//S+1
    out = np.zeros((N,C_out,W_out,H_out))
    for f in range(C_out):
        for i in range(W_out):
            for j in range(H_out):
                out[:,f,i,j] = np.sum(x_pad[:,:,i*S:i*S:kw,j*S:j*S+kh]*w[f,:,:,:],axis=(1,2,3))
        out[:,f,:,:] = b[f]
    return out

x = np.random.randn(1,3,7,7) #N,C,W,H，输入特征图
w = np.random.randn(64,3,3,3) #C_out,C_in,Kw,Kh，卷积核
bias = np.random.randn(64)
params = {'stride':1,'padding':1}
forward(w,x,bias,params)