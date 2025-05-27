import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def design_fir_filter(order, cutoff_freq, window='hamming'):
    """
    Thiết kế bộ lọc FIR sử dụng phương pháp cửa sổ.
    
    Parameters:
    -----------
    order : int
        Bậc của bộ lọc
    cutoff_freq : float
        Tần số cắt (0 < cutoff_freq < 1)
    window : str
        Loại cửa sổ ('hamming', 'hanning', 'blackman', etc.)
    
    Returns:
    --------
    b : ndarray
        Các hệ số của bộ lọc FIR
    """
    if not 0 < cutoff_freq < 1:
        raise ValueError("cutoff_freq phải nằm trong khoảng (0, 1)")
    
    b = signal.firwin(order, cutoff_freq, window=window)
    return b

def design_iir_filter(order, cutoff_freq, filter_type='butter'):
    """
    Thiết kế bộ lọc IIR sử dụng phép biến đổi song tuyến.
    
    Parameters:
    -----------
    order : int
        Bậc của bộ lọc
    cutoff_freq : float
        Tần số cắt (0 < cutoff_freq < 1)
    filter_type : str
        Loại bộ lọc ('butter', 'cheby1', 'cheby2', 'ellip')
    
    Returns:
    --------
    b, a : tuple
        Các hệ số của bộ lọc IIR (tử số và mẫu số)
    """
    if not 0 < cutoff_freq < 1:
        raise ValueError("cutoff_freq phải nằm trong khoảng (0, 1)")
    
    if filter_type == 'butter':
        b, a = signal.butter(order, cutoff_freq)
    elif filter_type == 'cheby1':
        b, a = signal.cheby1(order, 1, cutoff_freq)
    elif filter_type == 'cheby2':
        b, a = signal.cheby2(order, 40, cutoff_freq)
    elif filter_type == 'ellip':
        b, a = signal.ellip(order, 1, 40, cutoff_freq)
    else:
        raise ValueError("filter_type không hợp lệ")
    
    return b, a

def plot_frequency_response(b, a=None, fs=1.0):
    """
    Vẽ đồ thị đáp ứng tần số của bộ lọc.
    
    Parameters:
    -----------
    b : ndarray
        Các hệ số của bộ lọc (tử số cho IIR)
    a : ndarray, optional
        Các hệ số mẫu số cho bộ lọc IIR
    fs : float
        Tần số lấy mẫu
    """
    w, h = signal.freqz(b, a)
    plt.figure(figsize=(10, 6))
    
    # Vẽ đáp ứng biên độ
    plt.subplot(2, 1, 1)
    plt.plot(w/np.pi, 20 * np.log10(abs(h)))
    plt.grid(True)
    plt.xlabel('Tần số chuẩn hóa (×π rad/sample)')
    plt.ylabel('Biên độ (dB)')
    plt.title('Đáp ứng tần số')
    
    # Vẽ đáp ứng pha
    plt.subplot(2, 1, 2)
    plt.plot(w/np.pi, np.unwrap(np.angle(h)) * 180/np.pi)
    plt.grid(True)
    plt.xlabel('Tần số chuẩn hóa (×π rad/sample)')
    plt.ylabel('Pha (độ)')
    
    plt.tight_layout()
    plt.show()

def plot_impulse_response(b, a=None, n=50):
    """
    Vẽ đồ thị đáp ứng xung của bộ lọc.
    
    Parameters:
    -----------
    b : ndarray
        Các hệ số của bộ lọc (tử số cho IIR)
    a : ndarray, optional
        Các hệ số mẫu số cho bộ lọc IIR
    n : int
        Số điểm cần vẽ
    """
    if a is None:  # FIR filter
        h = b
    else:  # IIR filter
        h = signal.impulse((b, a), N=n)[1]
    
    plt.figure(figsize=(10, 4))
    plt.stem(range(len(h)), h)
    plt.grid(True)
    plt.xlabel('n')
    plt.ylabel('h[n]')
    plt.title('Đáp ứng xung')
    plt.show() 