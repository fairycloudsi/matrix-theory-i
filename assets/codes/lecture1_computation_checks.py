"""Lecture 1 numerical examples. Run: python3 lecture1_computation_checks.py
Requires NumPy. Checks identities, not hardware performance claims.
"""
import numpy as np


def check(label, actual, expected):
    np.testing.assert_allclose(actual, expected, atol=1e-12)
    print(f'{label}:\n{np.asarray(actual)}\n')


def haar(x):
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or x.size == 0 or x.size & (x.size - 1):
        raise ValueError('Use a nonempty vector of power-of-two length.')
    if x.size == 1:
        return x.copy()
    a = (x[::2] + x[1::2]) / np.sqrt(2)
    d = (x[::2] - x[1::2]) / np.sqrt(2)
    return np.concatenate((haar(a), d))


def inverse_haar(y):
    y = np.asarray(y, dtype=float)
    if y.size == 1:
        return y.copy()
    half = y.size // 2
    a, d = inverse_haar(y[:half]), y[half:]
    x = np.empty_like(y)
    x[::2], x[1::2] = (a + d) / np.sqrt(2), (a - d) / np.sqrt(2)
    return x


def main():
    check('E01 matrix multiplication', np.array([[1,2,0],[-1,3,1]]) @ np.array([[2,1],[0,-1],[4,2]]), [[2,-1],[2,-2]])
    x, y = np.array([1,-2,3]), np.array([4,0,-1])
    check('E02 dot product', x@y, 1)
    check('E03 AXPY', y+2*x, [6,-4,5])
    check('E04 gaxpy', np.array([1,0,-2])+np.array([[1,2],[-1,3],[2,0]])@np.array([2,-1]), [1,-5,2])
    check('E06 rank-one update', np.array([[1,0,1],[0,1,0]])+np.outer([1,2],[3,-1,2]), [[4,-1,3],[6,-1,4]])
    A, B = np.array([[1,2],[3,4]]), np.array([[5,6],[7,8]])
    check('E07 three equivalent views', sum(np.outer(A[:,k],B[k,:]) for k in range(2)), A@B)
    T = 2*np.eye(4)-np.eye(4,k=1)-np.eye(4,k=-1)
    check('E09 tridiagonal stencil', T@np.arange(1,5), [0,0,0,5])
    check('E10 triangular product', np.array([[1,2,3],[0,4,5],[0,0,6]])@np.array([[2,1,0],[0,3,2],[0,0,1]]), [[2,7,7],[0,12,13],[0,0,6]])
    band = np.array([[1,2,3,0,0],[4,5,6,7,0],[0,8,9,10,11],[0,0,12,13,14],[0,0,0,15,16]])
    packed = np.zeros((4,5), dtype=int)
    for j in range(5):
        for i in range(max(0,j-2),min(5,j+2)):
            packed[i-j+2,j]=band[i,j]
    check('E11 packed band (zeros mark padding)', packed, [[0,0,3,7,11],[0,2,6,10,14],[1,5,9,13,16],[4,8,12,15,0]])
    check('E11 band matvec', band@np.ones(5), [6,22,38,39,31])
    check('E12 symmetric matvec', np.array([[2,1,0],[1,3,4],[0,4,5]])@[1,2,3], [4,19,23])
    P=np.eye(3)[[2,0,1],:]
    check('E13 undo a permutation', P.T@P@np.array([10,20,30]), [10,20,30])
    I=np.eye(2); Z=np.zeros((2,2))
    check('E14 block product', np.block([[I,2*I],[Z,I]])@np.block([[3*I,I],[I,Z]]), np.block([[5*I,I],[I,Z]]))
    Bk=np.array([[1,2],[0,1]]); C=np.diag([2,3]); X=np.array([[1,2],[3,4]])
    check('E15-E16 vec identity (column stacking)', np.kron(Bk,C)@X.reshape(-1,order='F'), (C@X@Bk.T).reshape(-1,order='F'))
    J=np.array([[0,1],[-1,0]]); h=.5; S=np.array([[1,h],[0,1]]); M=np.array([[0,1],[-4,0]]); E=np.eye(2)+h*M
    check('E17 symplectic shear', S.T@J@S, J)
    check('E17 explicit Euler is not symplectic', E.T@J@E, 2*J)
    a,b,c,d=A.ravel(); e,f,g,h=B.ravel()
    m1,m2,m3,m4,m5,m6,m7=(a+d)*(e+h),(c+d)*e,a*(f-h),d*(g-e),(a+b)*h,(c-a)*(e+f),(b-d)*(g+h)
    check('E18 seven products', [m1,m2,m3,m4,m5,m6,m7], [65,35,-2,8,24,22,-30])
    check('E19 Strassen recombination', [[m1+m4-m5+m7,m3+m5],[m2+m4,m1-m2+m3+m6]], A@B)
    x=np.arange(1,5); ev=np.fft.fft(x[::2]); od=np.fft.fft(x[1::2]); tw=np.exp(-2j*np.pi*np.arange(2)/4)*od
    check('E20-E21 FFT butterfly', np.concatenate((ev+tw,ev-tw)), np.fft.fft(x))
    sine=np.sin(np.pi*np.outer(np.arange(1,4),np.arange(1,4))/4)
    check('E22 DST-I', sine@[1,0,-1], [0,2,0])
    check('E23 even extension DFT', np.fft.fft([1,2,1,2]), [6,0,-2,0])
    x=np.array([2,4,6,8]); y=haar(x)
    check('E24 Haar coefficients', y, [10,-4,-np.sqrt(2),-np.sqrt(2)])
    check('E25 inverse Haar', inverse_haar(y), x)
    approx=y.copy(); approx[2:]=0
    check('E25 fine-detail removal', inverse_haar(approx), [3,3,7,7])
    check('E25 energy', y@y, x@x)
    check('E25 error energy', np.sum((x-inverse_haar(approx))**2), 4)
    check('E26 column-major order', np.array([[1,2,3],[4,5,6]]).ravel(order='F'), [1,4,2,5,3,6])
    check('E28 cyclic loads', np.array([8,8,8,8,1,1,1,1]).reshape(2,4).sum(axis=0), [9,9,9,9])
    check('E29 speedup', 8/(8/4+.5), 3.2)
    result=np.zeros((2,2),dtype=int)
    for i in range(2):
        for j in range(2):
            for step in range(2):
                k=(i+j+step)%2
                result[i,j]+=A[i,k]*B[k,j]
    check('E30 Cannon inner-index schedule', result, A@B)
    print('All numerical checks passed.')


if __name__ == '__main__':
    main()
