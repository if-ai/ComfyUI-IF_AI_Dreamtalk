# ComfyUI-IF_AI_Dreamtalk
Talking avatars Heads for the IF_AI tools integrates dreamtalk in ComfyUI

## Prerequisites

  Fixed the windows error download FFMPEG if you don't have it yet  `ffmpeg -version`
   https://github.com/BtbN/FFmpeg-Builds/releases
  unziped on `C:\` or `C:\Program Files`
  Create a System environment PATH with pointing to the bin folder
  
  ![SystemPropertiesAdvanced_bpfdyGq1u6](https://github.com/if-ai/ComfyUI-IF_AI_tools/assets/21185218/a3b311c7-f266-42f2-aeaf-30990a26eb2c)

  for Linux 
  Thanks at @dlandry 
  
      ```bash     
        sudo apt install cmake
        sudo apt install libopenblas-dev
        sudo apt install build-essential
        sudo apt update
        sudo apt install ffmpeg
        open -e ~/.bash_profile
        export PATH="/usr/local/bin:$PATH"
        pip install cmake
        pip install dlib.
        ```

  Donwload the Dreamtalk models to your ComfyUI models folder should look like this /ComfyUI/models/dreamtalk/checkpoints/
  make sure it point to the correct location in your harddrive
   
     ```bash
        wget https://huggingface.co/camenduru/dreamtalk/resolve/main/damo/dreamtalk/checkpoints/denoising_network.pth -O /mnt/h/ComfyUI/models/dreamtalk/checkpoints/denoising_network.pth
        wget https://huggingface.co/camenduru/dreamtalk/resolve/main/damo/dreamtalk/checkpoints/renderer.pt -O /mnt/h/ComfyUI/models/dreamtalk/checkpoints/renderer.pt
        ```
## Support
If you find this tool useful, please consider supporting my work by:
- Starring the repository on GitHub: [ComfyUI-IF_AI_tools](https://github.com/if-ai/ComfyUI-IF_AI_tools)
- Subscribing to my YouTube channel: [Impact Frames](https://youtube.com/@impactframes?si=DrBu3tOAC2-YbEvc)
- Supporting me on Ko-fi: [Impact Frames Ko-fi](https://ko-fi.com/impactframes)
- Becoming a patron on Patreon: [Impact Frames Patreon](https://patreon.com/ImpactFrames)

Your support helps me bring updates and improvements faster!

## Related Tools
- [IF_prompt_MKR](https://github.com/if-ai/IF_prompt_MKR) - A similar tool available for Stable Diffusion WebUI
- [IF_AI_tools](https://github.com/if-ai/ComfyUI-IF_AI_tools) - LLM Nodes for chating and Creating SD prompts locally with Ollama or Via APIs

ComfyUI Integrations:
Deramtalk https://github.com/ali-vilab/dreamtalk


