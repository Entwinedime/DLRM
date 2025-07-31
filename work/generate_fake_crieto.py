import os
import random
import string
import argparse

def random_dense(prob_missing=0.2):
    if random.random() < prob_missing:
        return ""
    return str(random.randint(0, 10000))

def random_sparse(prob_missing=0.7):
    if random.random() < prob_missing:
        return ""
    length = 8
    return ''.join(random.choices("0123456789abcdef", k=length))

def generate_row(click_prob=0.4):
    label = "1" if random.random() < click_prob else "0"
    dense_features = [random_dense() for _ in range(13)]
    sparse_features = [random_sparse() for _ in range(26)]
    return "\t".join([label] + dense_features + sparse_features)

def generate_day_file(path, num_rows, click_prob):
    with open(path, "w") as f:
        for _ in range(num_rows):
            f.write(generate_row(click_prob) + "\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", type=str, required=True, help="Output directory for generated files")
    parser.add_argument("--days", type=int, default=24, help="Number of days to generate (default 24)")
    parser.add_argument("--rows_per_day", type=int, default=1000, help="Number of rows per file")
    parser.add_argument("--click_prob", type=float, default=0.4, help="Click-through rate")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    for day in range(args.days):
        filename = os.path.join(args.output_dir, f"day_{day}")
        print(f"Generating {filename}, rows: {args.rows_per_day}")
        generate_day_file(filename, args.rows_per_day, args.click_prob)

if __name__ == "__main__":
    main()