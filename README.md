# Multithreading Producer-Consumer

This project demonstrates a multithreading producer-consumer scenario using Python's `threading` and `queue` modules. The producer generates random integers and adds them to a shared queue, while the consumer retrieves and processes them.

## How to Run

### Prerequisites

Make sure you have Python installed on your system (Python 3.9 recommended).

### Steps to Run:

1. Clone this repository or download the script.
2. Navigate to the directory where the script is located.
3. Install required dependencies (if any) using:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the script:
   ```sh
   python3 Q1_multithreading.py 
   ```

The program will run for 10 seconds, producing and consuming random integers.

## Directory Structure

```
OpenNet_Q1/
│-- Q1_multithreading.py 
│-- requirements.txt 
│-- README.md  
│-- assets/
│   ├── OpenNet_Q1.gif 
```

## Dependencies

This project requires only standard Python libraries (`threading`, `queue`, `random`, `time`). If additional dependencies are needed in the future, they will be specified in `requirements.txt` or `pyproject.toml`.

### Example `requirements.txt`

```
python==3.9.0
# No external dependencies required
```

## Demo

Below is a GIF demonstrating the script running:

![](https://github.com/SharkBlahaj/OpenNet_Q1/blob/main/assets/OpenNet_Q1.gif)


The output will display produced and consumed numbers in real time.

---

For any questions, feel free to open an issue or contact the author!
