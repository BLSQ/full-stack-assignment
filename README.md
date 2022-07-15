# Bluesquare full-stack development assignment

This repo contains the instruction for the completion of the **Full stack developer** assignment.

This assignment takes the form of a **small realistic project**, to be developed as a little **single-page app**.

It will be used to assess your skill levels, and also your ability to work with modern development tool and 
practices, such as Git/Github, Docker, etc...

**We expect you to dedicate between 3-4 hours of work to this exercise**. It's ok if not everything is perfect or 100% 
finished, the idea is not to spend a lot of time on this but rather to see what you can build in a few hours.

## The project: a release checklist

The goal of this small assignment is to build a very small functional modern web application.

This application is a **release checklist tool** that could help developers with their release process.

![alt text](https://github.com/BLSQ/full-stack-assignment/blob/main/wireframes/releasecheck.png?raw=true)

You can find the above mock-ups in the `/wireframes` directory of this repository.

The application has only one main model : `Release`. A `Release` is composed of multiple `Step`s and has the 
following properties :

- A name (`text`, mandatory)
- A date (`datetime`, mandatory)
- A status (`planned|ongoing|done`, auto)
- Additional info (`text`, optional)

A release keeps track of the completion state of the different steps. A `Step` has only two states : on or off.

The `status` is not chosen by the end user, it is simply computed from the steps state :

- No step completed : `planned`
- At least one step completed : `ongoing`
- All steps completed : `done`

For the sake of this example, let's assume that a release is done in 7 to 10 steps. The mock-ups include few 
example steps but feel free to change them. 

To keep things simple, the steps are the same for every release and don't change over time - you don't need to 
have a database table to store each step, as long as you store, for each release, which step has been completed.

## Running the code

*This section should be updated with the required instructions to run your project*.

## Assignment tasks

### Must-have

In terms of features :

- [ ] Users should be able to view a list of all the releases
- [ ] Users should be able to create a new release (with a name, due date, and optional "additional information")
- [ ] Users should be able to check / uncheck the steps that are part of a release
- [ ] Users should be able to update the release additional information

In terms of technical constraints :

- [ ] The whole codebase should be contained in a single repository available on GitHub, which should be a fork 
      of this repository
- [ ] The end result should be a single-page application
- [ ] `React` should be used for the frontend, either with `create-react-app` or `nextjs`
- [ ] `Python` should be used for the backend (ideally with `Django` but `Flask` or `FastAPI` are ok too)
- [ ] The application state should be stored in a `PostgreSQL` or `MySQL` database
- [ ] The frontend and the backend should communicate using an API
- [ ] The app is styled with a few CSS rules, and should have a simple, usable UX (no time for fancy design stuff)
- [ ] There should be a small `README.md` file with the instructions needed to run the code locally

**Please note that this shouldn't be a multi-user application**. It does not need any kind of user management.

### Nice-to-have (if you have the time)

In terms of features :

- [ ] Users could be able to delete a release
- [ ] Users could benefit from a responsive interface

Regarding the tech :

- [ ] The frontend and backend could use `GraphQL` as the API layer
- [ ] The backend could be easily run locally with `Docker` (`Dockerfile` + `docker-compose.yaml`)
- [ ] The codebase could contain a couple of automated tests

## Where to start :

1. Fork this repository
1. Write the project code (3-4 hours)
1. Commit & push your code every now and then - we expect to see a reasonable amount of commits
1. Update this `README.md` file with installation instructions (see "Running the code" above)
1. That's it - we'll review your work together once you are done
