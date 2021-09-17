"""Turkish-BQuAD: Biology Question Answering Dataset for Turkish Language."""


import json

import datasets
from datasets.tasks import QuestionAnsweringExtractive


logger = datasets.logging.get_logger(__name__)


_CITATION = """\
@article{2021akyon,
       author = {{Akyon}, Kerem B. and {Akyon}, Ela N. and {Akyon},
                 Fatih C.,
        title = "{Turkish-BQuAD: Biology Question Answering Dataset for Turkish Language}",
      journal = {Github},
         year = 2021,
}
"""

_DESCRIPTION = """\
Biology Question Answering Dataset for Turkish Language (Turkish-BQuAD) is a reading comprehension \
dataset, consisting of questions posed by Kerem and Ela on a set of MEB \
Biology textbooks, where the answer to every question is a segment of text, or span, \
from the corresponding reading passage, or the question might be unanswerable.
"""

_URL = "https://raw.githubusercontent.com/TurQuest/turkish-bquad/main/2018%20%2B%202020%20veri%20k%C3%BCmesi/"
_URLS = {
    "train": _URL + "turkish-bquad-train-v1.json",
    "dev": _URL + "turkish-bquad-valid-v1.json",
}


class TurkishBquadConfig(datasets.BuilderConfig):
    """BuilderConfig for TurkishBQUAD."""

    def __init__(self, **kwargs):
        """BuilderConfig for TurkishBQUAD.

        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(TurkishBquad, self).__init__(**kwargs)


class TurkishBquad(datasets.GeneratorBasedBuilder):
    """Turkish-BQuAD: Biology Question Answering Dataset for Turkish Language. Version 1.0."""

    BUILDER_CONFIGS = [
        TurkishBquadConfig(
            name="plain_text",
            version=datasets.Version("1.0.0", ""),
            description="Plain text",
        ),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "title": datasets.Value("string"),
                    "context": datasets.Value("string"),
                    "question": datasets.Value("string"),
                    "answers": datasets.features.Sequence(
                        {
                            "text": datasets.Value("string"),
                            "answer_start": datasets.Value("int32"),
                        }
                    ),
                }
            ),
            # No default supervised_keys (as we have to pass both question
            # and context as input).
            supervised_keys=None,
            homepage="https://github.com/TurQuest/turkish-bquad/",
            citation=_CITATION,
            task_templates=[
                QuestionAnsweringExtractive(
                    question_column="question",
                    context_column="context",
                    answers_column="answers",
                )
            ],
        )

    def _split_generators(self, dl_manager):
        downloaded_files = dl_manager.download_and_extract(_URLS)

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={"filepath": downloaded_files["train"]},
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                gen_kwargs={"filepath": downloaded_files["dev"]},
            ),
        ]

    def _generate_examples(self, filepath):
        """This function returns the examples in the raw (text) form."""
        logger.info("generating examples from = %s", filepath)
        key = 0
        with open(filepath, encoding="utf-8") as f:
            squad = json.load(f)
            for article in squad["data"]:
                title = article.get("title", "")
                for paragraph in article["paragraphs"]:
                    context = paragraph[
                        "context"
                    ]  # do not strip leading blank spaces GH-2585
                    for qa in paragraph["qas"]:
                        answer_starts = [
                            answer["answer_start"] for answer in qa["answers"]
                        ]
                        answers = [answer["text"] for answer in qa["answers"]]
                        # Features currently used are "context", "question", and "answers".
                        # Others are extracted here for the ease of future expansions.
                        yield key, {
                            "title": title,
                            "context": context,
                            "question": qa["question"],
                            "id": qa["id"],
                            "answers": {
                                "answer_start": answer_starts,
                                "text": answers,
                            },
                        }
                        key += 1
