# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/04_evaluation.ipynb (unless otherwise specified).

__all__ = []

# Cell
import os
import re
import json
import numpy as np
from pathlib import Path
from functools import partial

# Cell
import torch
from datasets import load_metric
from dataclasses import dataclass, field
from transformers import Wav2Vec2Processor
from typing import Any, Dict, List, Optional, Union

# Cell
import os
import re
import json
import numpy as np
from pathlib import Path
from functools import partial

# Cell
import torch
from datasets import load_metric
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union