# Thiết kế và Mô phỏng Bộ lọc FIR và IIR
##Digital Signal Processing project
Dự án này cung cấp các công cụ để thiết kế và mô phỏng các bộ lọc FIR (Finite Impulse Response) và IIR (Infinite Impulse Response) trong Python.

## Cài đặt

1. Clone repository này
2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Cấu trúc dự án

- `filter_design.py`: Chứa các hàm thiết kế bộ lọc FIR và IIR
- `filter_simulation.py`: Chứa các hàm mô phỏng và phân tích bộ lọc
- `utils.py`: Chứa các hàm tiện ích

## Tính năng

- Thiết kế bộ lọc FIR sử dụng phương pháp cửa sổ
- Thiết kế bộ lọc IIR sử dụng phép biến đổi song tuyến
- Mô phỏng đáp ứng tần số
- Mô phỏng đáp ứng xung
- Phân tích độ trễ nhóm
- Vẽ đồ thị đáp ứng tần số và pha

## Sử dụng

```python
from filter_design import design_fir_filter, design_iir_filter
from filter_simulation import simulate_filter

# Thiết kế bộ lọc FIR
fir_filter = design_fir_filter(order=64, cutoff_freq=0.2)

# Thiết kế bộ lọc IIR
iir_filter = design_iir_filter(order=4, cutoff_freq=0.2)

# Mô phỏng bộ lọc
response = simulate_filter(filter_coeffs, input_signal)
``` 
