

import numpy as np 
import matplotlib.pyplot as plt
from scipy import fftpack

x = np.zeros(500)
x[100:150] = 1

X = fftpack.fft(x)
print(np.abs(X))

f, (ax0, ax1) = plt.subplots(2, 1, sharex=True)

ax0.plot(x)
ax0.set_ylim(-0.1, 1.1)

ax1.plot(fftpack.fftshift(np.abs(X)))
ax1.set_ylim(-5, 55)
plt.show()

"""
[(5.00000000e+01) (4.91819058e+01) (4.67756953e+01) (4.29222263e+01)
 (3.78453205e+01) (3.18362252e+01) (2.52335343e+01) (1.84000823e+01)
 (1.16985417e+01) 5.46753374e+00 4.30211422e-16 4.47461453e+00
 7.80313526e+00 9.91556478e+00 (1.08257662e+01) (1.06260538e+01)
 9.47628802e+00 7.58848359e+00 5.20825873e+00 2.59466300e+00
 1.89877351e-15 2.34878957e+00 4.26579587e+00 5.61775292e+00
 6.33085563e+00 6.39245322e+00 5.84771946e+00 4.79180530e+00
 3.35833036e+00 1.70533756e+00 1.28157444e-15 1.59657889e+00
 2.94319418e+00 3.92988799e+00 4.48596520e+00 4.58414386e+00
 4.24066210e+00 3.51151963e+00 2.48536044e+00 1.27377566e+00
 7.41423330e-16 1.21292191e+00 2.25341918e+00 3.03113887e+00
 3.48433696e+00 3.58434365e+00 3.33681488e+00 2.77978164e+00
 1.97879788e+00 1.01973937e+00 1.38777878e-16 9.81048315e-01
 1.83142843e+00 2.47490554e+00 2.85757412e+00 2.95213479e+00
 2.75954169e+00 2.30795374e+00 1.64917414e+00 8.52989253e-01
 3.92523115e-16 8.26338781e-01 1.54770302e+00 2.09816022e+00
 2.43004728e+00 2.51795370e+00 2.36048976e+00 1.97973529e+00
 1.41848429e+00 7.35604600e-01 7.10889596e-16 7.16218946e-01
 1.34469012e+00 1.82722068e+00 2.12107965e+00 2.20268926e+00
 2.06940425e+00 1.73925641e+00 1.24873665e+00 6.48870653e-01
 1.15677834e-15 6.34206084e-01 1.19292193e+00 1.62392851e+00
 1.88842872e+00 1.96447670e+00 1.84872362e+00 1.55634860e+00
 1.11921867e+00 5.82489123e-01 2.77555756e-16 5.71067932e-01
 1.07575281e+00 1.46655135e+00 1.70784371e+00 1.77909549e+00
 1.67655310e+00 1.41329768e+00 1.01768184e+00 5.30327859e-01
 3.55444798e-16 5.21233768e-01 9.83074684e-01 1.34181018e+00
 1.56441704e+00 1.63156876e+00 1.53927607e+00 1.29902516e+00
 9.36423995e-01 4.88510229e-01 3.51083347e-16 4.81145532e-01
 9.08399408e-01 1.24114013e+00 1.44848789e+00 1.51214586e+00
 1.42798734e+00 1.20625375e+00 8.70363834e-01 4.54467915e-01
 9.15513360e-16 4.48426647e-01 8.47376128e-01 1.15877552e+00
 1.35352815e+00 1.41421356e+00 1.33662520e+00 1.13001225e+00
 8.16018170e-01 4.26434361e-01 9.15513360e-16 4.21431628e-01
 7.96982777e-01 1.09069898e+00 1.27497527e+00 1.33313591e+00
 1.26092778e+00 1.06679539e+00 7.70924029e-01 4.03156965e-01
 5.66104887e-16 3.98987441e-01 7.55059367e-01 1.03403182e+00
 1.20955171e+00 1.26557446e+00 1.19781866e+00 1.01406698e+00
 7.33295237e-01 3.83725281e-01 2.77555756e-16 3.80237742e-01
 7.20025715e-01 9.86663715e-01 1.15484987e+00 1.20907204e+00
 1.14502915e+00 9.69953138e-01 7.01809640e-01 3.67464160e-01
 3.55444798e-16 3.64545285e-01 6.90703953e-01 9.47019041e-01
 1.10906933e+00 1.16178828e+00 1.10085743e+00 9.33046167e-01
 6.75472564e-01 3.53864972e-01 4.91046260e-16 3.51428708e-01
 6.66203216e-01 9.13904630e-01 1.07084505e+00 1.12232624e+00
 1.06401034e+00 9.02275226e-01 6.53526596e-01 3.42540031e-01
 7.10889596e-16 3.40520439e-01 6.45842650e-01 8.86407857e-01
 1.03913214e+00 1.08961586e+00 1.03349663e+00 8.76819006e-01
 6.35390482e-01 3.33191665e-01 1.75541673e-16 3.31538002e-01
 6.29098838e-01 8.63826910e-01 1.01312689e+00 1.06283392e+00
 1.00855362e+00 8.56045502e-01 6.20616940e-01 3.25590822e-01
 2.77555756e-17 3.24264106e-01 6.15569251e-01 8.45622247e-01
 9.92211682e-01 1.04134809e+00 9.88595801e-01 8.39469874e-01
 6.08863095e-01 3.19562067e-01 2.50666042e-16 3.18532649e-01
 6.04946537e-01 8.31382419e-01 9.75916153e-01 1.02467755e+00
 9.73178694e-01 8.26724690e-01 5.99869594e-01 3.14972970e-01
 2.98936698e-16 3.14218823e-01 5.97000350e-01 8.20799909e-01
 9.63889799e-01 1.01246513e+00 9.61973234e-01 8.17538923e-01
 5.93445880e-01 3.11726637e-01 1.75541673e-16 3.11232157e-01
 5.91564575e-01 8.13654180e-01 9.55882752e-01 1.00445782e+00
 9.54747945e-01 8.11723338e-01 5.89459967e-01 3.09756536e-01
 4.16333634e-17 3.09511733e-01 5.88528589e-01 8.09800124e-01
 9.51732748e-01 1.00049368e+00 9.51356965e-01 8.09160740e-01
 5.87831665e-01 3.09023094e-01 0.00000000e+00 3.09023094e-01
 5.87831665e-01 8.09160740e-01 9.51356965e-01 1.00049368e+00
 9.51732748e-01 8.09800124e-01 5.88528589e-01 3.09511733e-01
 4.16333634e-17 3.09756536e-01 5.89459967e-01 8.11723338e-01
 9.54747945e-01 1.00445782e+00 9.55882752e-01 8.13654180e-01
 5.91564575e-01 3.11232157e-01 1.75541673e-16 3.11726637e-01
 5.93445880e-01 8.17538923e-01 9.61973234e-01 1.01246513e+00
 9.63889799e-01 8.20799909e-01 5.97000350e-01 3.14218823e-01
 2.98936698e-16 3.14972970e-01 5.99869594e-01 8.26724690e-01
 9.73178694e-01 1.02467755e+00 9.75916153e-01 8.31382419e-01
 6.04946537e-01 3.18532649e-01 2.50666042e-16 3.19562067e-01
 6.08863095e-01 8.39469874e-01 9.88595801e-01 1.04134809e+00
 9.92211682e-01 8.45622247e-01 6.15569251e-01 3.24264106e-01
 2.77555756e-17 3.25590822e-01 6.20616940e-01 8.56045502e-01
 1.00855362e+00 1.06283392e+00 1.01312689e+00 8.63826910e-01
 6.29098838e-01 3.31538002e-01 1.75541673e-16 3.33191665e-01
 6.35390482e-01 8.76819006e-01 1.03349663e+00 1.08961586e+00
 1.03913214e+00 8.86407857e-01 6.45842650e-01 3.40520439e-01
 7.10889596e-16 3.42540031e-01 6.53526596e-01 9.02275226e-01
 1.06401034e+00 1.12232624e+00 1.07084505e+00 9.13904630e-01
 6.66203216e-01 3.51428708e-01 4.91046260e-16 3.53864972e-01
 6.75472564e-01 9.33046167e-01 1.10085743e+00 1.16178828e+00
 1.10906933e+00 9.47019041e-01 6.90703953e-01 3.64545285e-01
 3.55444798e-16 3.67464160e-01 7.01809640e-01 9.69953138e-01
 1.14502915e+00 1.20907204e+00 1.15484987e+00 9.86663715e-01
 7.20025715e-01 3.80237742e-01 2.77555756e-16 3.83725281e-01
 7.33295237e-01 1.01406698e+00 1.19781866e+00 1.26557446e+00
 1.20955171e+00 1.03403182e+00 7.55059367e-01 3.98987441e-01
 5.66104887e-16 4.03156965e-01 7.70924029e-01 1.06679539e+00
 1.26092778e+00 1.33313591e+00 1.27497527e+00 1.09069898e+00
 7.96982777e-01 4.21431628e-01 9.15513360e-16 4.26434361e-01
 8.16018170e-01 1.13001225e+00 1.33662520e+00 1.41421356e+00
 1.35352815e+00 1.15877552e+00 8.47376128e-01 4.48426647e-01
 9.15513360e-16 4.54467915e-01 8.70363834e-01 1.20625375e+00
 1.42798734e+00 1.51214586e+00 1.44848789e+00 1.24114013e+00
 9.08399408e-01 4.81145532e-01 3.51083347e-16 4.88510229e-01
 9.36423995e-01 1.29902516e+00 1.53927607e+00 1.63156876e+00
 1.56441704e+00 1.34181018e+00 9.83074684e-01 5.21233768e-01
 3.55444798e-16 5.30327859e-01 1.01768184e+00 1.41329768e+00
 1.67655310e+00 1.77909549e+00 1.70784371e+00 1.46655135e+00
 1.07575281e+00 5.71067932e-01 2.77555756e-16 5.82489123e-01
 1.11921867e+00 1.55634860e+00 1.84872362e+00 1.96447670e+00
 1.88842872e+00 1.62392851e+00 1.19292193e+00 6.34206084e-01
 1.15677834e-15 6.48870653e-01 1.24873665e+00 1.73925641e+00
 2.06940425e+00 2.20268926e+00 2.12107965e+00 1.82722068e+00
 1.34469012e+00 7.16218946e-01 7.10889596e-16 7.35604600e-01
 1.41848429e+00 1.97973529e+00 2.36048976e+00 2.51795370e+00
 2.43004728e+00 2.09816022e+00 1.54770302e+00 8.26338781e-01
 3.92523115e-16 8.52989253e-01 1.64917414e+00 2.30795374e+00
 2.75954169e+00 2.95213479e+00 2.85757412e+00 2.47490554e+00
 1.83142843e+00 9.81048315e-01 1.38777878e-16 1.01973937e+00
 1.97879788e+00 2.77978164e+00 3.33681488e+00 3.58434365e+00
 3.48433696e+00 3.03113887e+00 2.25341918e+00 1.21292191e+00
 7.41423330e-16 1.27377566e+00 2.48536044e+00 3.51151963e+00
 4.24066210e+00 4.58414386e+00 4.48596520e+00 3.92988799e+00
 2.94319418e+00 1.59657889e+00 1.28157444e-15 1.70533756e+00
 3.35833036e+00 4.79180530e+00 5.84771946e+00 6.39245322e+00
 6.33085563e+00 5.61775292e+00 4.26579587e+00 2.34878957e+00
 1.89877351e-15 2.59466300e+00 5.20825873e+00 7.58848359e+00
 9.47628802e+00 1.06260538e+01 (1.08257662e+01) 9.91556478e+00
 7.80313526e+00 4.47461453e+00 4.30211422e-16 5.46753374e+00
 (1.16985417e+01) (1.84000823e+01) (2.52335343e+01) (3.18362252e+01)
 (3.78453205e+01) (4.29222263e+01) (4.67756953e+01) (4.91819058e+01)]
"""