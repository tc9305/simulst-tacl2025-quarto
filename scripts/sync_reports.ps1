# Publish the existing self-contained reports without editing contributor originals.
$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$reports = @(
    'Liu/report.html',
    'chiu/seamless_streaming_progress.html'
)

# Validate all inputs before copying. These reports currently embed their resources.
foreach ($report in $reports) {
    $source = Join-Path $repoRoot $report
    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) {
        throw "Missing rendered report: $report. Render it with Quarto first."
    }
}
foreach ($report in $reports) {
    $source = Join-Path $repoRoot $report
    $destination = Join-Path (Join-Path $repoRoot 'docs') $report
    New-Item -ItemType Directory -Path (Split-Path -Parent $destination) -Force | Out-Null
    Copy-Item -LiteralPath $source -Destination $destination -Force
    Write-Output "Published docs/$report"
}
