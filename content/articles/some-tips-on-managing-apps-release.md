---
Title: What I learned managing weekly release for a 50M+ users’ app
Date: 2020-08-22 12:12
Tags: release, management, tips
Slug: some-tips-on-managing-apps-release
Version: 1.1.0
Status: Published
Summary: In any war, game, or enterprise resource management, the last thing you want is to underestimate your opponent(s). In release management, the opponent is “chaos”. The last thing a release manager should expect is that everything, from bug-free features to timely completion of production builds will be done as per the cadence schedule.
---


# What I learned managing weekly release for 50M+ users’ app

_Disclaimer: Everything here are my personal observations, experiences, commentary, or “wisdom”. My past, present, or future employers shouldn’t be held responsible for it.
Also, take in or apply the stuff below “with a grain of salt”._

![releases](https://i.imgur.com/BE87UxPl.jpg){: .noZoom}

> In any war, game, or enterprise resource management, the last thing you want is to underestimate your opponent(s). In release management, the opponent is “chaos”.

The last thing a release manager should expect is that everything, from bug-free features to timely completion of production builds will be done as per the cadence schedule.

Here is something that I had to learn over time. It might help someone, somewhere.


### Is the “release cadence” effective?

Not all apps are created equal, neither for the exact same consumer base nor with the same feature set. So, THE perfect release cadence or frequency doesn’t exist. Every app needs to find it’s own pace. The frequency might be feature-based, the target market base, fixed calendar-based, and/or mix of those.

Though I can’t go in detail for each of them, I emphasize going through the process of identifying the right frequency. While for the passenger app of Grab, due to the sheer number of features (or change of features) and bug fixes, it makes sense to roll out a new version every week, it might make no sense for your app that gets new features once in a month or two that has a limited number of enterprise customers and your user-support team has to train them in sessions.

Ask the questions across the company who are involved or have a vested interest in the release process.



*   Who are the primary users? And, who can be considered secondary?
*   Are the primary audience tech-savvy enough to be excited to navigate the new changes, or will they be pissed about the frequent changes?
*   How frequently may the product teams push out new features?
*   How resilient the quality assurance team is to exhaustively verify the new features and look out for new bugs that are going to break the old, stable features?
*   How much automation is in place to support a more frequent build, release, and rollout?

Particularly, if your QA/testing team isn’t well-distributed as per the app scopes, to provide the final sign-off on that specific scope, avoid intense weekly releases. Having a shiny process, just for the sake of having it, is an easy recipe for disaster.


### Is the process well-documented & communicated?

Well-accepted process documents should work as the org-wide “release” manifesto, well discussed among the contributing teams and agreed by the stakeholders. 

Once the process and agreed upon process timeline is there, in case of confusion or conflict between the teams, the release team will have two clear paths to move forward.

*   It’s already in the doc, point to it.
*   If it’s not in the doc or not clear enough, an opportunity to improve

If there is an exception, foreseeable disruption, or any upcoming change in the process, _communicate early_, and _communicate frequently_.


### Is some automation possible? 

Identify the opportunities to automate. As a release manager, if you need something to do more than twice a day, start there. Have you been asked the same question twice? Include the answer in a FAQ doc.

Document the need, identify the tool required. It can be as simple as a SQL query, a Python script, or a much more complex system. 

Before jumping headfirst into the thing, identify the matrix to monitor the improvement, and get approval (at least, verbally) from the stakeholders.

Some example automation tool I use:



*   [Google script](https://www.google.com/script/start/) to monitor changes on Google Sheet
*   [Slack bot response](https://slack.com/help/articles/202026038-An-introduction-to-Slackbot) for selected keywords
*   Python scripts for compiling custom JIRA reports. [An example](https://gist.github.com/kmonsoor/62ed1bc6cd3084648245073744182227)
*   [Email forwarding to Slack DM](https://slack.com/intl/en-sg/help/articles/206819278-Send-emails-to-Slack)

Automation paves the path to sustainable scalability. The release manager might be able to ping (aka “pull info or update”) three persons, but definitely shouldn’t try for thirty. So, establish some “push notification” mechanism as much as possible. E.g., comment on the Google _Sheet_ or more frequent status update on the JIRA ticket, etc.


### Is proper “Divide & Conquer” in place?

This DC method/mechanism/scheme (as a fan of the Marvel universe, I don’t mind the name mixup though :P ) is a controversial term. However, the “division of labor” is a well-established example. Regardless of the name and the flavor, it’s essential for the successful execution of any high-frequency release cycle. 



*   Design the process and its breakdown based on the roles, not the actual persons or their skillset
*   Minimize switching between roles for individual persons in a single release cycle. e.g., if someone, in the QA team, is writing test cases, let them do that for at least the period. If someone is testing individual features at the beginning of the week, let her continue it until the end of the release.  \
_Well-designed repetition is key to reaching excellence._
*   Keep only integrated test (staging, then production) dependency for release rollout. For individual features, the developing team(s) should take care of it, before “signing off” it ready for shipping. The “not ready to be shipped” features must be isolated from the production scope, excluding it from the ongoing release cycle.
*   Imagine the shipment process of a newer version as a concept like a train and different teams as different product pipelines. Products come to the train station only when it’s packed and ready to be shipped. I believe it's an agile concept, as well.
*   Like a public train, the release “train” should depart as per schedule. If any feature is delayed due to unforeseen reasons or a recently discovered severe bug, the release-train should not wait for it. Instead, once the feature is stabilized later, it should wait for the next _train_.
*   Adopting the concept of a train and its scheduled departure and well-documented checkpoints (i.e., phases) enables a large organization to expect and likewise communicate what to expect when.


### Are you deploying on a wrong moon-phase?

Probably, it should be a piece of common knowledge. Be it a backend deployment or app rollout on app stores; please avoid changing anything with the “production” tag, before a weekend or a multi-day holiday. 

Like the [printer meme](https://twitter.com/System32Comics/status/1266100094853476352/photo/1), the universe likes to throw unique, unforeseen issues after weekend deployments. It’s a mystery of the world, I guess.


### Is there a provision for backup?

Plan capacity with some slack. 

I’d suggest going for the 80/20 rule, meaning the weekly release should go out, even in the unavailability of 20% human resources. 

Unlike machines, people will be sick, go out for vacation, emergency travel plans, unexpectedly resign, etc. anything can happen. So, like any other robust system design, plan for “disaster”. 


### Is proper Continuous Integration/Deployment (CI/CD) in place?

To have an efficient release process, automated and well-documented CI/CD pipeline is almost a prerequisite.



*   Developers across the board should be able to build, test, merge their code, and build the binary from the latest stable and/or release checkpoints.
*   Once their change, be it a feature or a bugfix, is ready to be merged with the release branch, a complete suite of automated tests should run on the resultant binary to detect any regression bug due to the change; with no dependency on the release team.
*   QA, while testing for a particular release, should be able to receive regression or production build without any manual effort from the release team.


### Is there continuous feedback established?

An efficient release process is an intensive process. And, no process can be perfect from the beginning. 

Every organization has, as its fingerprint, has different priorities, deliverables, audience, resources, and of course, budget. So, while the release cycle can start with an agile blueprint, down the line it needs to be well fit on its organizational body. 

Here comes the necessity for continuous feedback from the participants, stakeholders, and even the release team-members.


### Stay on the “good book” of the app stores ;)

If the app is in the center of revenue of your company, keep a close eye on the regular comm from the app stores, i.e., Google Play and Apple Appstore. It’s very easy to miss these communications, among other day-to-day stuff.

Regardless of how ridiculous your company feels about some policies on the app stores, please read between the lines. In case of confusion, read again. Especially if you’re one of the big fishes.  
If a particular app store weren’t strictly monitoring or enforcing some policies last month, don’t even think they aren’t going to enforce tomorrow and reject your app. 

The release manager or the team, being the interface with the app stores, should frequently communicate with the stakeholders and the product team to carefully go through relevant app store policies long before they invest company time and resources into a feature or a roadmap. Trust me; it happens more than anyone likes to admit that after month-long design and development, the app update with the feature gets rejected on the app stores, solely due to this new feature.

If possible, try to get hold of and build a working relationship with the business development or dev support teams of Google and Apple. It might help in case of any misunderstanding and/or some negotiations about the compliance timeline.  
I can’t go into any more detail though ;)


### Notes:



*   Please don’t take the number 50M+ literally. The actual number is much higher but should be considered as company secrets ;). Right?
*   This article is NOT a definitive process guide, and I’m not an expert on Agile methodologies. I’m just trying to share my learning from my release experience of 1.75 years. Some stuff might help any other release manager on the other side of the planet. That’s the goal here.

Thanks, y’all.
