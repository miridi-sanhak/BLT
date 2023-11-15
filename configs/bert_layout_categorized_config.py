# coding=utf-8
# Copyright 2023 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Default Hyperparameter configuration."""

import ml_collections


def get_config():
  """Gets the default hyperparameter configuration."""

  config = ml_collections.ConfigDict()
  # Exp info
  config.dataset_path = "/home/work/increased_en_data/BLT/data2/"
  config.dataset = "CATEGORIZED"
  config.vocab_size = 154
  config.experiment = "bert_layout"
  config.model_class = "bert_layout"
  config.image_size = 256
  config.composition = "default" # default, ltwh, ltrb
  config.sort_by = "top_left_to_bottom_right" # top_left_to_bottom_right, distance_from_center

  # Training info
  config.seed = 0
  config.layout_dim = 2
  config.log_every_steps = 100
  config.eval_num_steps = 1000
  config.max_length = 128
  config.batch_size = 64
  config.train_shuffle = True
  config.eval_pad_last_batch = False
  config.eval_batch_size = 64
  config.num_train_steps = 50_000
  config.checkpoint_every_steps = 5000
  config.eval_every_steps = 1000
  config.num_eval_steps = 100

  # Model info
  config.dtype = "float32"
  config.autoregressive = False
  config.shuffle_buffer_size = 10
  config.use_vae = True
  config.share_embeddings = True
  config.num_layers = 4
  config.qkv_dim = 512
  config.emb_dim = 512
  config.mlp_dim = 2048
  config.num_heads = 8
  config.dropout_rate = 0.3
  config.attention_dropout_rate = 0.1
  config.restore_checkpoints = True
  config.label_smoothing = 0.0
  config.sampling_method = "top-p"
  config.use_vertical_info = False
  # config.test_checkpoint_dir = "/home/work/increased_en_data/BLT/exp3_get_low_loss/checkpoints"

  # Optimizer info
  config.optimizer = ml_collections.ConfigDict()
  config.optimizer.type = "adam"
  config.optimizer.warmup_steps = 4000
  config.optimizer.lr = 5e-3
  config.optimizer.beta1 = 0.9
  config.optimizer.beta2 = 0.98
  config.optimizer.weight_decay = 0.01
  config.beta_rate = 1 / 20_000

  return config
