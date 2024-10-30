# Path to the Notepad executable
$notepadPath = "C:\Windows\notepad.exe"

# Loop indefinitely
while ($true) {
    # Generate a timestamp for the filename
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $filePath = "C:\Users\$env:USERNAME\Documents\NotepadOutput_$timestamp.txt"

    # Start Notepad
    Start-Process -FilePath $notepadPath -ArgumentList $filePath

    # Wait for a moment to allow Notepad to open
    Start-Sleep -Seconds 1

    # Write to the file
    Add-Content -Path $filePath -Value "This is a message written at $timestamp"

    # Wait before the next iteration
    Start-Sleep -Seconds .5

    # Optional: Close Notepad (if you want to automate closing)
    # Get-Process -Name "notepad" | Stop-Process
}

