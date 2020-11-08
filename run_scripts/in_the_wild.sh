python create_test_dataset.py --data $1 --n_samples $2
CUDA_VISIBLE_DEVICES=0 python test.py --name males_model --which_epoch latest --display_id 0 --traverse --image_path_file males_image_list.txt --in_the_wild --deploy --interp_step 1 --loadSize 256 --fineSize 256

