from dmriprep.workflows.dwi_mrtrix.pipelines.epi_ref.edges import (
    CONVERSION_TO_OUTPUT_EDGES,
    DWIEXTRACT_TO_MRMATH_EDGES,
    INPUT_TO_DWIEXTRACT_EDGES,
    MRMATH_TO_CONVERSION_EDGES,
    MRMATH_TO_OUTPUT_EDGES,
)
from dmriprep.workflows.dwi_mrtrix.pipelines.epi_ref.nodes import (
    DWIEXTRACT_NODE,
    DWIREF_CONVERSION_NODE,
    INPUT_NODE,
    MRMATH_NODE,
    OUTPUT_NODE,
)
from niworkflows.engine.workflows import LiterateWorkflow as Workflow

EPI_REF = [
    (INPUT_NODE, DWIEXTRACT_NODE, INPUT_TO_DWIEXTRACT_EDGES),
    (DWIEXTRACT_NODE, MRMATH_NODE, DWIEXTRACT_TO_MRMATH_EDGES),
    (MRMATH_NODE, OUTPUT_NODE, MRMATH_TO_OUTPUT_EDGES),
    (MRMATH_NODE, DWIREF_CONVERSION_NODE, MRMATH_TO_CONVERSION_EDGES),
    (DWIREF_CONVERSION_NODE, OUTPUT_NODE, CONVERSION_TO_OUTPUT_EDGES),
]


def init_epi_ref_wf(name: str = "epi_reference_wf") -> Workflow:
    """
    Initiate a workflow for generation of EPI referance image

    Parameters
    ----------
    name : str, optional
        Workflow's name, by default "epi_reference_wf"

    Returns
    -------
    pe.Workflow
        Initiated workflow
    """
    wf = Workflow(name=name)
    wf.connect(EPI_REF)
    return wf
