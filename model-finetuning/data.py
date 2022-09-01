from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from torch.utils.data import Dataset
from transformers import PreTrainedTokenizerBase


@dataclass
class TextFileDataset(Dataset):
    filenames: list[str]
    tokenizer: PreTrainedTokenizerBase
    max_length: int = 2048

    def __len__(self) -> int:
        return len(self.filenames)

    def __getitem__(self, index: int) -> dict[str, Any]:
        with open(self.filenames[index]) as fp:
            text = fp.read()
        encodings = self.tokenizer(text, max_length=self.max_length, truncation=True)
        encodings["labels"] = encodings["input_ids"]
        return encodings
