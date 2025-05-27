import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def group_delay(b, a=None, w=None):
    """
    Tính toán độ trễ nhóm của bộ lọc.
    
    Parameters:
    -----------
    b : ndarray
        Các hệ số của bộ lọc (tử số cho IIR)
    a : ndarray, optional
        Các hệ số mẫu số cho bộ lọc IIR
    w : ndarray, optional
        Tần số góc để tính toán độ trễ nhóm
    
    Returns:
    --------
    w : ndarray
        Tần số góc
    gd : ndarray
        Độ trễ nhóm
    """
    if w is None:
        w = np.linspace(0, np.pi, 512)
    
    if a is None:
        a = np.array([1.0])
    
    w, gd = signal.group_delay((b, a), w=w)
    return w, gd

def plot_group_delay(b, a=None):
    """
    Vẽ đồ thị độ trễ nhóm của bộ lọc.
    
    Parameters:
    -----------
    b : ndarray
        Các hệ số của bộ lọc (tử số cho IIR)
    a : ndarray, optional
        Các hệ số mẫu số cho bộ lọc IIR
    """
    w, gd = group_delay(b, a)
    
    plt.figure(figsize=(10, 4))
    plt.plot(w/np.pi, gd)
    plt.grid(True)
    plt.xlabel('Tần số chuẩn hóa (×π rad/sample)')
    plt.ylabel('Độ trễ nhóm (mẫu)')
    plt.title('Độ trễ nhóm')
    plt.show()

def analyze_filter(b, a=None):
    """
    Phân tích toàn diện bộ lọc.
    
    Parameters:
    -----------
    b : ndarray
        Các hệ số của bộ lọc (tử số cho IIR)
    a : ndarray, optional
        Các hệ số mẫu số cho bộ lọc IIR
    """
    # Đảm bảo a là numpy array với kiểu dữ liệu phù hợp
    if a is None:
        a = np.array([1.0], dtype=np.float64)
    else:
        a = np.asarray(a, dtype=np.float64)
    
    # Đảm bảo b là numpy array với kiểu dữ liệu phù hợp
    b = np.asarray(b, dtype=np.float64)
    
    # Vẽ đáp ứng tần số
    w, h = signal.freqz(b, a)
    plt.figure(figsize=(12, 8))
    
    # Đáp ứng biên độ
    plt.subplot(3, 1, 1)
    plt.plot(w/np.pi, 20 * np.log10(abs(h)))
    plt.grid(True)
    plt.xlabel('Tần số chuẩn hóa (×π rad/sample)')
    plt.ylabel('Biên độ (dB)')
    plt.title('Đáp ứng tần số')
    
    # Đáp ứng pha
    plt.subplot(3, 1, 2)
    plt.plot(w/np.pi, np.unwrap(np.angle(h)) * 180/np.pi)
    plt.grid(True)
    plt.xlabel('Tần số chuẩn hóa (×π rad/sample)')
    plt.ylabel('Pha (độ)')
    
    # Độ trễ nhóm
    plt.subplot(3, 1, 3)
    w, gd = group_delay(b, a)
    plt.plot(w/np.pi, gd)
    plt.grid(True)
    plt.xlabel('Tần số chuẩn hóa (×π rad/sample)')
    plt.ylabel('Độ trễ nhóm (mẫu)')
    
    plt.tight_layout()
    plt.show()

def zero_pole_plot(b, a=None):
    """
    Vẽ đồ thị điểm không và điểm cực của bộ lọc.
    
    Parameters:
    -----------
    b : ndarray
        Các hệ số của bộ lọc (tử số cho IIR)
    a : ndarray, optional
        Các hệ số mẫu số cho bộ lọc IIR
    """
    if a is None:
        a = np.array([1.0], dtype=np.float64)
    else:
        a = np.asarray(a, dtype=np.float64)
    
    b = np.asarray(b, dtype=np.float64)
    
    z, p, k = signal.tf2zpk(b, a)
    
    plt.figure(figsize=(8, 8))
    plt.plot(np.real(z), np.imag(z), 'o', label='Điểm không')
    plt.plot(np.real(p), np.imag(p), 'x', label='Điểm cực')
    
    # Vẽ đường tròn đơn vị
    circle = plt.Circle((0, 0), 1, fill=False, linestyle='--')
    plt.gca().add_artist(circle)
    
    plt.grid(True)
    plt.axis('equal')
    plt.xlabel('Thực')
    plt.ylabel('Ảo')
    plt.title('Đồ thị điểm không và điểm cực')
    plt.legend()
    plt.show() 