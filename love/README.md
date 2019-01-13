# Love

Draw a heart using a name.

## How to build

When build, set main.love or "Love" will be used as default.

`go build -ldflags="-X main.love=<name>" love.go`

## How to run

`go run -ldflags="-X main.love=<name>" love.go`
