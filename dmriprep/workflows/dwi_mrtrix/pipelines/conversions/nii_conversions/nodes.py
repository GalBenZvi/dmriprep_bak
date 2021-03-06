import nipype.pipeline.engine as pe
from dmriprep.workflows.dwi_mrtrix.pipelines.conversions.nii_conversions.configurations import (
    COREG_DWI_CONVERSION_KWARGS,
    INPUTNODE_FIELDS,
    NATIVE_DWI_CONVERSION_KWARGS,
    OUTPUTNODE_FIELDS,
)
from nipype.interfaces import mrtrix3 as mrt
from nipype.interfaces import utility as niu

INPUT_NODE = pe.Node(
    niu.IdentityInterface(fields=INPUTNODE_FIELDS),
    name="inputnode",
)
OUTPUT_NODE = pe.Node(
    niu.IdentityInterface(fields=OUTPUTNODE_FIELDS),
    name="outputnode",
)
NATIVE_DWI_CONVERSION_NODE = pe.Node(
    mrt.MRConvert(**NATIVE_DWI_CONVERSION_KWARGS),
    name="native_dwi_conversion",
)
COREG_DWI_CONVERSION_NODE = pe.Node(
    mrt.MRConvert(**COREG_DWI_CONVERSION_KWARGS),
    name="coreg_dwi_conversion",
)
