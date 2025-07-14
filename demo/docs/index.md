# MkDocs Kuma Uptime Badge Plugin Demo

This is a demonstration of the MkDocs Kuma Uptime Badge Plugin, which converts shorthand placeholders to full Uptime Kuma badge links during the build.

## Basic Example

Here's a basic status badge:

{{uptime id=1}}

## With Custom Labels

Here's a status badge with custom labels:

{{uptime id=2 upLabel="Online" downLabel="Offline"}}

## With Custom Colors

Here's a status badge with custom colors:

{{uptime id=3 upColor="green" downColor="red"}}

Check out the [Examples](examples.md) page for more advanced usage.
