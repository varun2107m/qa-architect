from fastapi import APIRouter, HTTPException
import traceback

from backend.app.api.schemas.generation import PromptRequest
from backend.app.agents.orchestration_agent import generate_from_prompt

router = APIRouter()


@router.post("/generate")
def generate_framework_route(request: PromptRequest):

    try:

        print("\n=== REQUEST ===\n")
        print(request)

        result = generate_from_prompt(
            request.prompt,
            request.output_dir
        )

        print("\n=== RESULT ===\n")
        print(result)

        # -----------------------------
        # SAFE RESPONSE NORMALIZATION
        # -----------------------------
        if isinstance(result, dict):

            # If already structured correctly, enhance it
            if "analysis" in result:

                return {
                    "analysis": result.get("analysis"),
                    "generation": {
                        "status": "success",
                        "mode": "AI_ARCHITECT_MODE",
                        "output_dir": result.get("output_dir", request.output_dir)
                    }
                }

            # fallback structure
            return {
                "analysis": result,
                "generation": {
                    "status": "success",
                    "mode": "AI_ARCHITECT_MODE",
                    "output_dir": request.output_dir
                }
            }

        # If result is not dict (edge case)
        return {
            "analysis": {
                "raw_output": str(result)
            },
            "generation": {
                "status": "success",
                "mode": "AI_ARCHITECT_MODE",
                "output_dir": request.output_dir
            }
        }

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    