import torch
import torch.nn as nn
import torch.nn.functional as F
from .sr_decoder_noBN_noD import Decoder
from .edsr import EDSR, EDSR_RFA
from .rcan import RCAN



class DeepLab(nn.Module):
    def __init__(self, ch, c1=128, c2=512, srmode='EDSR', factor=2, sync_bn=True, freeze_bn=False):
        super().__init__()

        self.sr_decoder = Decoder(c1, c2)
        if srmode=='EDSR':
            self.sr_network = EDSR(num_channels=ch, input_channel=64, factor=8) #factor=4 #factor=8
        elif srmode=="RCAN":
            self.sr_network = RCAN(num_channels=ch, input_channel=64, factor=8, ResidualGroupsnumber=4, RCABsnumber=4) #num_channels=3, input_channel=64, ResidualGroupsnumber=10, RCABsnumber=20,  factor=4, width=64, reduction=16, conv=default_conv

        self.factor = factor
        self.srmode = srmode


    def forward(self, x):
        x, low_level_feat = x[-1], x[-2]
        x_sr = self.sr_decoder(x, low_level_feat, self.factor)
        x_sr_up = self.sr_network(x_sr)

        return x_sr_up


if __name__ == "__main__":
    model = DeepLab(backbone='mobilenet', output_stride=16)
    model.eval()
    input = torch.rand(1, 3, 513, 513)
    output = model(input)
    print(output.size())


