# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
#
# Copyright 2021 The NiPreps Developers <nipreps@gmail.com>
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
#
# We support and encourage derived works from this project, please read
# about our expectations at
#
#     https://www.nipreps.org/community/licensing/
#
"""py.test configuration."""
import os
import tempfile
from pathlib import Path
import numpy as np
import nibabel as nb
import pytest
from dipy.data.fetcher import _make_fetcher, UW_RW_URL

_dipy_datadir_root = os.getenv("DMRIPREP_TESTS_DATA") or Path.home()
dipy_datadir = Path(_dipy_datadir_root) / ".cache" / "data"
dipy_datadir.mkdir(parents=True, exist_ok=True)

_make_fetcher(
    "fetch_sherbrooke_3shell",
    str(dipy_datadir),
    UW_RW_URL + "1773/38475/",
    ["HARDI193.nii.gz", "HARDI193.bval", "HARDI193.bvec"],
    ["HARDI193.nii.gz", "HARDI193.bval", "HARDI193.bvec"],
    [
        "0b735e8f16695a37bfbd66aab136eb66",
        "e9b9bb56252503ea49d31fb30a0ac637",
        "0c83f7e8b917cd677ad58a078658ebb7",
    ],
    doc="Download a 3shell HARDI dataset with 192 gradient direction",
)()

_sherbrooke_data = {
    "dwi_file": dipy_datadir / "HARDI193.nii.gz",
    "bvecs": np.loadtxt(dipy_datadir / "HARDI193.bvec").T,
    "bvals": np.loadtxt(dipy_datadir / "HARDI193.bval"),
}


@pytest.fixture(autouse=True)
def doctest_autoimport(doctest_namespace):
    """Make available some fundamental modules to doctest modules."""
    doctest_namespace["np"] = np
    doctest_namespace["nb"] = nb
    doctest_namespace["os"] = os
    doctest_namespace["Path"] = Path
    doctest_namespace["data_dir"] = Path(__file__).parent / "data" / "tests"
    doctest_namespace["dipy_datadir"] = dipy_datadir
    tmpdir = tempfile.TemporaryDirectory()
    doctest_namespace["tmpdir"] = tmpdir.name
    yield
    tmpdir.cleanup()


@pytest.fixture()
def dipy_test_data(scope="session"):
    """Create a temporal directory shared across tests to pull data in."""
    return _sherbrooke_data
