# slave-agent-plugins — the external plugins home

The user-installable capability store for
[slave-agent](https://github.com/khaalidrafi/slave-agent). The core
ships plugin **machinery only**; every integration payload — messaging,
storefronts, platform adapters, anything "merely useful" — lives here,
and the user decides which of it to install (specs/013, Owner ruling
2026-11-22: *"user will add them via plugins as they wish. That's light
core."*).

## Layout

    plugins/
      <name>/
        plugin.yaml      # manifest: name, version, entry points, tools
        README.org       # what it does, configuration, honest limits
        ...              # the code, once a plugin leaves charter stage
        tests/           # plugin tests (run via the core's test runner)

A plugin entry that has no code yet is a **charter**: a README that
states the contract it will implement. Nothing here ships stub code.

## Installing

Plugins are configured per profile in slave-agent's `config.yaml`:

    plugins.entries.<name>.settings.<key>: <value>

and enabled by installing the plugin directory into the agent's plugin
path (or pointing the plugin path at a checkout of this repo). Each
plugin's README documents its settings.

## Laws (inherited from the core)

- **Secrets travel as env var names only.** A plugin reads credentials
  through `agent.secret_scope` at call time — never at import, never in
  chat, files, commits or logs.
- **Read-only before write.** No outward-facing write path (messages,
  order mutations) lands before an approve-before-send gate exists.
- **Money never routes through a model.** Numbers a tool returns are the
  integration's own API fields; the only arithmetic is counting rows,
  with provenance.
- **One process, many profiles.** Adapters cache per (settings, token)
  so profiles never inherit each other's connections.

## Current entries

| Plugin     | Stage    | What it gives the agent                                  |
|------------|----------|----------------------------------------------------------|
| `shop`     | transferred | Read-only, config-driven REST storefront adapter (order queue, orders, order, catalog) + `hermes shop` / `/shop`. Code + tests live here; installed via the core's plugin catalog. |
| `whatsapp` | charter  | WhatsApp messaging bridge (read + gated send).           |
| `telegram` | charter  | Telegram messaging bridge (read + gated send).           |

## Commit law

Same as the core repo: author as the model that did the work
(`MODEL <MODEL@PROVIDER>`), trailers
`Co-authored-by: z.ai-agent <z.ai-agent@z.ai>` and
`Co-authored-by: Khalid Rafi <khaalidrafi@gmail.com>`, never commit to
`main` directly (`ai/<topic>` or `ai/main`).
