from filter_design import design_fir_filter, design_iir_filter, plot_frequency_response, plot_impulse_response
from filter_simulation import simulate_filter, generate_test_signal, plot_signals, plot_spectrum
from utils import analyze_filter, zero_pole_plot

def main():
    # Thiết kế bộ lọc FIR
    print("Thiết kế bộ lọc FIR...")
    fir_filter = design_fir_filter(order=64, cutoff_freq=0.2)
    
    # Thiết kế bộ lọc IIR
    print("Thiết kế bộ lọc IIR...")
    iir_filter_b, iir_filter_a = design_iir_filter(order=4, cutoff_freq=0.2)
    
    # Phân tích bộ lọc FIR
    print("\nPhân tích bộ lọc FIR:")
    analyze_filter(fir_filter)
    zero_pole_plot(fir_filter)
    
    # Phân tích bộ lọc IIR
    print("\nPhân tích bộ lọc IIR:")
    analyze_filter(iir_filter_b, iir_filter_a)
    zero_pole_plot(iir_filter_b, iir_filter_a)
    
    # Tạo tín hiệu thử nghiệm
    print("\nTạo tín hiệu thử nghiệm...")
    t, input_signal = generate_test_signal(freq=[10, 50, 100], duration=1.0)
    
    # Mô phỏng bộ lọc FIR
    print("\nMô phỏng bộ lọc FIR...")
    fir_output = simulate_filter(fir_filter, None, input_signal)
    plot_signals(t, input_signal, fir_output)
    plot_spectrum(fir_output)
    
    # Mô phỏng bộ lọc IIR
    print("\nMô phỏng bộ lọc IIR...")
    iir_output = simulate_filter(iir_filter_b, iir_filter_a, input_signal)
    plot_signals(t, input_signal, iir_output)
    plot_spectrum(iir_output)

if __name__ == "__main__":
    main() 