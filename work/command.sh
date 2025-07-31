python3 generate_fake_crieto.py --output_dir crieto_fake
python3 ../tools/criteo1t_parquet.py --input_dir crieto_fake --output crieto_parquet --spark_tmp_dir spark --export_dataset_info