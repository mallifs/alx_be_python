def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom= float(denominator)

        result = num / denom
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except ValueError:
        return "Error: Non-numeric input provided"
    except Exception as e:
        return f"Unexpected error occured: {str(e)}"
    return f"The result is: {result:.2f}"

        