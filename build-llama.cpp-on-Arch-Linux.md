LOG: [LEARN] Guide: Build llama.cpp on Arch Linux with UV

**Title:** Build llama.cpp on Arch Linux in a UV Virtual Environment
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** build-llama.cpp-on-Arch-Linux.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### Prerequisites
- Arch Linux
- Git, CMake, CUDA toolkit (optional)
- UV package manager

### Step 1: Install Dependencies
```bash
$ sudo pacman -S git cmake nvidia-cuda-toolkit python uv
```

### Step 2: Clone Repository
```bash
$ git clone https://github.com/ggerganov/llama.cpp.git
$ cd llama.cpp
```

### Step 3: Create UV Virtual Environment
```bash
$ uv venv .venv
$ source .venv/bin/activate
```

### Step 4: Configure Build (with CUDA)
```bash
$ cmake -B build -DGGML_CUDA=ON
```

### Step 5: Build
```bash
$ cmake --build build --config Release
```

### Step 6: Run Model
```bash
# CLI mode
$ ./build/bin/llama-cli -m path/to/model.gguf -n 512 -ngl 32

# Server mode
$ ./build/bin/llama-server -m path/to/model.gguf -n 512 -ngl 32
```

## The "Blueprint" (The Why/Logic)

### Why UV?
- Fast, Rust-based package manager
- Virtual environments via `uv venv`
- Compatible with pip/requirements.txt

### llama.cpp Architecture
- `llama-cli` — command-line inference
- `llama-server` — OpenAI-compatible API server
- GGML backend — CPU/GPU acceleration

### CUDA Support
- `-DGGML_CUDA=ON` enables NVIDIA GPU offload
- `-ngl` layers to offload (32 = all for 7B models)

## The "Deep Dive" (The Technical Root)

### Build Options
| Option | Description |
|--------|-------------|
| `-DGGML_CUDA=ON` | NVIDIA CUDA |
| `-DGGML_METAL=ON` | Apple Metal |
| `-DGGML_VULKAN=ON` | Vulkan/AMD |
| `-DGGML_BLAS=ON` | BLAS acceleration |

### Quantization
Models use GGUF format with quantization (Q4_K_M, Q8_0, etc.) for efficient inference.

### UV vs pip/venv
```bash
# UV (faster, single binary)
$ uv venv .venv
$ uv pip install -r requirements.txt

# Traditional
$ python -m venv .venv
$ .venv/bin/pip install -r requirements.txt
```

### References
- [llama.cpp GitHub](https://github.com/ggerganov/llama.cpp)
- [UV Documentation](https://docs.astral.sh/uv/)
- [Arch Wiki: CUDA](https://wiki.archlinux.org/title/CUDA)