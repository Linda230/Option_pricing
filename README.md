# Option_pricing
The code for Asian option pricing

You should first install "openturns" so that you can use the Halton, Faure and Sobol low discrepancy sequences. 

you can install "openturns" by the following command:

pip install openturns

Implementation details:
you can run the "low_discrepancy.py" to obtain the Moro-normalized Sobol sequence.

If you want to obtain the figure 1, 2 and 3, you can run the file of "sobol_normal.py".

To obtain the price of arithmetic average Asian option, you can run the file of "option_pricing.py". If you want to calculate the price of Asian option using the Monte Carlo simulation, you need to replace the Moro-normalized Sobol sequence with the random standard normal data.
