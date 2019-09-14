# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Public library API."""

from neural_tangents.utils.monte_carlo import get_ker_fun_monte_carlo
from neural_tangents.utils.empirical import get_ntk_fun_empirical
from neural_tangents.utils.empirical import get_nngp_fun_empirical
from neural_tangents.utils.empirical import get_ker_fun_empirical
from neural_tangents.utils.empirical import linearize
from neural_tangents.utils.empirical import taylor_expand
from neural_tangents.utils.batch import batch
from neural_tangents.utils import predict
from neural_tangents import stax