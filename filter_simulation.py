import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def simulate_filter(b, a, input_signal):
    """
    Mô phỏng bộ lọc với tín hiệu đầu vào.
    
    Parameters:
    -----------
    b : ndarray
        Các hệ số của bộ lọc (tử số cho IIR)
    a : ndarray, optional
        Các hệ số mẫu số cho bộ lọc IIR
    input_signal : ndarray
        Tín hiệu đầu vào
    
    Returns:
    --------
    output_signal : ndarray
        Tín hiệu đầu ra sau khi lọc
    """
    if a is None:  # FIR filter
        output_signal = signal.lfilter(b, 1, input_signal)
    else:  # IIR filter
        output_signal = signal.lfilter(b, a, input_signal)
    
    return output_signal

def generate_test_signal(freq, duration, fs=1000):
    """
    Tạo tín hiệu thử nghiệm.
    
    Parameters:
    -----------
    freq : float or list
        Tần số của tín hiệu (hoặc danh sách các tần số)
    duration : float
        Thời lượng của tín hiệu (giây)
    fs : float
        Tần số lấy mẫu
    
    Returns:
    --------
    t : ndarray
        Mảng thời gian
    signal : ndarray
        Tín hiệu được tạo
    """
    t = np.arange(0, duration, 1/fs)
    
    if isinstance(freq, (list, tuple, np.ndarray)):
        signal = np.zeros_like(t)
        for f in freq:
            signal += np.sin(2 * np.pi * f * t)
    else:
        signal = np.sin(2 * np.pi * freq * t)
    
    return t, signal

def plot_signals(t, input_signal, output_signal):
    """
    Vẽ đồ thị tín hiệu đầu vào và đầu ra.
    
    Parameters:
    -----------
    t : ndarray
        Mảng thời gian
    input_signal : ndarray
        Tín hiệu đầu vào
    output_signal : ndarray
        Tín hiệu đầu ra
    """
    plt.figure(figsize=(12, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(t, input_signal)
    plt.grid(True)
    plt.xlabel('Thời gian (s)')
    plt.ylabel('Biên độ')
    plt.title('Tín hiệu đầu vào')
    
    plt.subplot(2, 1, 2)
    plt.plot(t, output_signal)
    plt.grid(True)
    plt.xlabel('Thời gian (s)')
    plt.ylabel('Biên độ')
    plt.title('Tín hiệu đầu ra')
    
    plt.tight_layout()
    plt.show()

def plot_spectrum(signal, fs=1000):
    """
    Vẽ phổ tần số của tín hiệu.
    
    Parameters:
    -----------
    signal : ndarray
        Tín hiệu cần phân tích
    fs : float
        Tần số lấy mẫu
    """
    n = len(signal)
    f = np.fft.fftfreq(n, 1/fs)
    spectrum = np.abs(np.fft.fft(signal))
    
    plt.figure(figsize=(10, 4))
    plt.plot(f[:n//2], spectrum[:n//2])
    plt.grid(True)
    plt.xlabel('Tần số (Hz)')
    plt.ylabel('Biên độ')
    plt.title('Phổ tần số')
    plt.show() 