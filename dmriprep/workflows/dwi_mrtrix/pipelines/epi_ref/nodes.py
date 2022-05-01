"""
Nodes' configurations for *epi_ref* pipelines.
"""
import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi_mrtrix.pipelines.epi_ref.configurations import (
    CONVERSION_KWARGS,
    DWIEXTRACT_KWARGS,
    INPUT_NODE_FIELDS,
    MRMATH_KWARGS,
    OUTPUT_NODE_FIELDS,
)
from nipype.interfaces import mrtrix3 as mrt
from nipype.interfaces import utility as niu
from niworkflows.engine.workflows import LiterateWorkflow as Workflow

#: i/o
INPUT_NODE = pe.Node(
    niu.IdentityInterface(fields=INPUT_NODE_FIELDS),
    name="inputnode",
)
OUTPUT_NODE = pe.Node(
    niu.IdentityInterface(fields=OUTPUT_NODE_FIELDS),
    name="outputnode",
)

#: Building blocks
DWIEXTRACT_NODE = pe.Node(
    mrt.DWIExtract(**DWIEXTRACT_KWARGS), name="dwiextract"
)

MRMATH_NODE = pe.Node(
    mrt.MRMath(**MRMATH_KWARGS),
    name="mrmath",
)
DWIREF_CONVERSION_NODE = pe.Node(
    mrt.MRConvert(**CONVERSION_KWARGS),
    name="dwiref_conversion",
)
