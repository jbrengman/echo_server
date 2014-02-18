Feature: Echo Server
	Implement an echo server that recieves a message from the echo client and sends the same message back to the client.

	Scenario: Echo message
		Given the message <send>
		When I call main
		Then I receive the message <receive>

	Examples:
		| send				| receive			|
		| test				| test				|
		| test message #2	| test message #2	|
		| This is a really long test message. I hope it doesn't break anything...	| This is a really long test message. I hope it doesn't break anything...	|
		| !@#$%^&*()233456789][pk/nbv,<>;':"|\'	| !@#$%^&*()233456789][pk/nbv,<>;':"|\'	|