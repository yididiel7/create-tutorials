LOG: [LEARN] Reference: Warp Terminal API Key

**Title:** Warp Key
**Date:** 2026-02-13 (10:30:00 Asia/Jerusalem)
**Author:** Sr. Yididiel Hills, Arch Linux Admin, Developer
**lfnc:** warp_key.md
**Copyright:** © 2026-2027 Sr. Tyrone Hills
**License:** MIT – see LICENSE file for details

## The "Recipe" (The How)

### API Key
```
wk-1.<YOUR_WARP_API_KEY_HERE>
```

### Usage
```bash
# Set as environment variable
export WARP_API_KEY="wk-1.<YOUR_WARP_API_KEY_HERE>"

# Or add to ~/.zshrc
echo 'export WARP_API_KEY="wk-1.<YOUR_WARP_API_KEY_HERE>"' >> ~/.zshrc
```

### Security Notes
- **Never commit** API keys to version control
- Use `.zshrc-personal` or `.env` files (gitignored)
- Rotate keys periodically
- Store in password manager (pass, 1Password, Bitwarden)

## The "Blueprint" (The Why/Logic)

### Warp API
- Warp Terminal cloud features
- Team sync, workflows, AI features
- Key format: `wk-1.<hex>`

### Best Practices
```bash
# Use password manager
pass insert warp/api-key

# Or use direnv
echo 'export WARP_API_KEY="..."' > .envrc
direnv allow
```

## The "Deep Dive" (The Technical Root)

### Key Format
```
wk-1.<base64_encoded_payload>
# Prefix: wk-1 = Warp Key v1
# Payload: 64-char hex = 256-bit key
```

### Rotation
```bash
# Generate new key at https://app.warp.dev/settings/keys
# Update all environments
# Revoke old key
```

### References
- [Warp Documentation](https://docs.warp.dev/)
- [Warp API Keys](https://app.warp.dev/settings/keys)
